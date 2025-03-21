import json
from typing import List, Dict, Any, Optional, Union
import html


class ActionHistoryBeautifier:
    """Utility to convert browser action history into a readable format."""

    @staticmethod
    def get_action_type(action_dict: Dict[str, Any]) -> str:
        """Extract the action type from the action dictionary."""
        # The action type is the first key that's not 'interacted_element'
        for key in action_dict:
            if key != 'interacted_element':
                return key
        return 'unknown'

    @staticmethod
    def extract_element_details(dom_element) -> Dict[str, Any]:
        """Extract relevant details from a DOM history element."""
        if dom_element is None:
            return None

        return {
            "tag_name": getattr(dom_element, 'tag_name', None),
            "xpath": getattr(dom_element, 'xpath', None),
            "highlight_index": getattr(dom_element, 'highlight_index', None),
            "attributes": getattr(dom_element, 'attributes', {}),
            "css_selector": getattr(dom_element, 'css_selector', None),
            "parent_path": getattr(dom_element, 'entire_parent_branch_path', [])
        }

    @staticmethod
    def beautify_action(action_dict: Dict[str, Any]) -> Dict[str, Any]:
        """Convert a single action dictionary into a beautified format."""
        action_type = ActionHistoryBeautifier.get_action_type(action_dict)
        action_details = action_dict.get(action_type, {})
        element_details = ActionHistoryBeautifier.extract_element_details(
            action_dict.get('interacted_element')
        )

        # Convert to a more structured format
        beautified = {
            "action": {
                "type": action_type,
                **action_details
            }
        }

        if element_details:
            beautified["element"] = element_details

        return beautified

    @staticmethod
    def beautify_actions(actions: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """Convert a list of action dictionaries into a beautified format."""
        return [ActionHistoryBeautifier.beautify_action(action) for action in actions]

    @staticmethod
    def format_as_json(actions: List[Dict[str, Any]], indent: int = 2) -> str:
        """Format the beautified actions as a JSON string."""
        return json.dumps(actions, indent=indent)

    @staticmethod
    def format_as_markdown(actions: List[Dict[str, Any]]) -> str:
        """Format the beautified actions as Markdown."""
        md = "# Action History\n\n"

        for i, action in enumerate(actions):
            action_type = action.get("action", {}).get("type", "unknown")
            action_index = action.get("action", {}).get("index", "")

            # Add a header for the action
            md += f"## {i+1}. {action_type.replace('_', ' ').title()} (Index: {action_index})\n\n"

            # Add action details
            md += "### Action Details\n"
            md += "```json\n"
            md += json.dumps(action.get("action", {}), indent=2)
            md += "\n```\n\n"

            # Add element details if present
            if "element" in action and action["element"]:
                md += "### Element Details\n"

                # Add a table with key element properties
                md += "| Property | Value |\n"
                md += "|----------|-------|\n"

                element = action["element"]

                # Add tag and id
                md += f"| **Tag** | `{element.get('tag_name', 'N/A')}` |\n"

                # Add id if present in attributes
                if element.get('attributes', {}).get('id'):
                    md += f"| **ID** | `{element['attributes']['id']}` |\n"

                # Add class if present in attributes
                if element.get('attributes', {}).get('class'):
                    md += f"| **Class** | `{element['attributes']['class']}` |\n"

                # Add type if present in attributes
                if element.get('attributes', {}).get('type'):
                    md += f"| **Type** | `{element['attributes']['type']}` |\n"

                # Add xpath
                if element.get('xpath'):
                    md += f"| **XPath** | `{element['xpath']}` |\n"

                # Add simplified xpath (using id if available)
                if element.get('attributes', {}).get('id'):
                    simplified_xpath = f"//*[@id='{element['attributes']['id']}']"
                    md += f"| **Simplified XPath** | `{simplified_xpath}` |\n"

                md += "\n"

                # Add full element details in a collapsible section
                md += "<details>\n"
                md += "<summary>Full Element Details</summary>\n\n"
                md += "```json\n"
                md += json.dumps(element, indent=2)
                md += "\n```\n"
                md += "</details>\n\n"

            md += "---\n\n"

        return md

    @staticmethod
    def format_as_html(actions: List[Dict[str, Any]]) -> str:
        """Format the beautified actions as HTML."""
        html_content = """
        <!DOCTYPE html>
        <html>
        <head>
            <title>Action History</title>
            <style>
                body { font-family: Arial, sans-serif; margin: 20px; }
                .action { margin-bottom: 30px; border: 1px solid #ddd; padding: 15px; border-radius: 5px; }
                .action-header { background-color: #f5f5f5; padding: 10px; margin-bottom: 15px; border-radius: 3px; }
                .element { margin-top: 15px; }
                .element-table { width: 100%; border-collapse: collapse; }
                .element-table th, .element-table td { 
                    padding: 8px; text-align: left; border-bottom: 1px solid #ddd; 
                }
                .element-table th { background-color: #f9f9f9; }
                pre { background-color: #f9f9f9; padding: 10px; border-radius: 3px; overflow-x: auto; }
                .input-secret { color: #999; font-style: italic; }
                details { margin-top: 10px; }
                summary { cursor: pointer; color: #0066cc; }
            </style>
        </head>
        <body>
            <h1>Action History</h1>
        """

        for i, action in enumerate(actions):
            action_type = action.get("action", {}).get("type", "unknown")
            action_index = action.get("action", {}).get("index", "")

            # Handle secret input text specially
            action_text = ""
            if action_type == "input_text" and "<secret>" in str(action.get("action", {}).get("text", "")):
                action_text = '<span class="input-secret">[SECRET TEXT]</span>'

            html_content += f"""
            <div class="action">
                <div class="action-header">
                    <h2>{i+1}. {action_type.replace('_', ' ').title()} (Index: {action_index}) {action_text}</h2>
                </div>
                
                <h3>Action Details</h3>
                <pre>{html.escape(json.dumps(action.get("action", {}), indent=2))}</pre>
            """

            if "element" in action and action["element"]:
                element = action["element"]
                html_content += """
                <div class="element">
                    <h3>Element Details</h3>
                    <table class="element-table">
                        <tr>
                            <th>Property</th>
                            <th>Value</th>
                        </tr>
                """

                # Add tag
                html_content += f"""
                        <tr>
                            <td><strong>Tag</strong></td>
                            <td><code>{element.get('tag_name', 'N/A')}</code></td>
                        </tr>
                """

                # Add id if present
                if element.get('attributes', {}).get('id'):
                    html_content += f"""
                        <tr>
                            <td><strong>ID</strong></td>
                            <td><code>{element['attributes']['id']}</code></td>
                        </tr>
                    """

                # Add class if present
                if element.get('attributes', {}).get('class'):
                    html_content += f"""
                        <tr>
                            <td><strong>Class</strong></td>
                            <td><code>{element['attributes']['class']}</code></td>
                        </tr>
                    """

                # Add type if present
                if element.get('attributes', {}).get('type'):
                    html_content += f"""
                        <tr>
                            <td><strong>Type</strong></td>
                            <td><code>{element['attributes']['type']}</code></td>
                        </tr>
                    """

                # Add XPath
                if element.get('xpath'):
                    html_content += f"""
                        <tr>
                            <td><strong>XPath</strong></td>
                            <td><code>{html.escape(element['xpath'])}</code></td>
                        </tr>
                    """

                # Add simplified XPath if ID is available
                if element.get('attributes', {}).get('id'):
                    simplified_xpath = f"//*[@id='{element['attributes']['id']}']"
                    html_content += f"""
                        <tr>
                            <td><strong>Simplified XPath</strong></td>
                            <td><code>{html.escape(simplified_xpath)}</code></td>
                        </tr>
                    """

                html_content += """
                    </table>
                    
                    <details>
                        <summary>View Full Element Details</summary>
                        <pre>{}</pre>
                    </details>
                </div>
                """.format(html.escape(json.dumps(element, indent=2)))

            html_content += """
            </div>
            """

        html_content += """
        </body>
        </html>
        """

        return html_content

    @staticmethod
    def beautify(actions: List[Dict[str, Any]], format: str = 'json', indent: int = 2) -> str:
        """
        Convert the action history into a beautified format.

        Args:
            actions: The output of history.model_actions()
            format: The output format ('json', 'markdown', or 'html')
            indent: The indentation level for JSON format

        Returns:
            The beautified action history in the specified format
        """
        beautified = ActionHistoryBeautifier.beautify_actions(actions)

        if format.lower() == 'json':
            return ActionHistoryBeautifier.format_as_json(beautified, indent)
        elif format.lower() == 'markdown' or format.lower() == 'md':
            return ActionHistoryBeautifier.format_as_markdown(beautified)
        elif format.lower() == 'html':
            return ActionHistoryBeautifier.format_as_html(beautified)
        else:
            raise ValueError(
                f"Unsupported format: {format}. Use 'json', 'markdown', or 'html'.")
