import asyncio
from browser_use import Browser, BrowserConfig, BrowserContextConfig, Controller, Agent, ActionResult
from browser_use.browser.context import BrowserContext
from llm import llm
from data.instructions import example_test_steps
from pydantic import BaseModel
from typing import List, Optional
import json
from action_util import ActionHistoryBeautifier
from service.error_handler import register_error_handlers
from service.routes import register_routes
from flask import Flask, jsonify
from flask_cors import CORS


class Post(BaseModel):
    xpath: Optional[str] = None
    tag_name: Optional[str] = None
    index: int


controller = Controller(output_model=Post)

browser = Browser(
    config=BrowserConfig(
        chrome_instance_path='/Applications/Google Chrome.app/Contents/MacOS/Google Chrome',
        headless=False,
        disable_security=True,
    )
)

initial_actions = [
    {
        'open_tab': {'url': 'https://edusoftweb.hcmiu.edu.vn/'}
    }
]

sensitive_data: dict[str, str] = {
    'type': 'Vietnamese',
    'Tên đăng nhập': 'ITITWE19021',
    'Mật khẩu': 'vuduy0913876222'
}

agent = Agent(
    task=example_test_steps,
    llm=llm,
    initial_actions=initial_actions,
    browser=browser,
    controller=controller,
    sensitive_data={
        'Tên đăng nhập': 'ITITWE19021',
        'Mật khẩu': 'vuduy0913876222'
    }
)


def create_app():
    app = Flask(__name__)
    CORS(app)
    register_routes(app)
    register_error_handlers(app)
    return app


async def main():
    app = create_app()
    app.run(debug=True, host='localhost', port=9092)
    # history = await agent.run()

    # # Get the model actions
    # model_actions = history.model_actions()

    # # Format the history in different ways
    # json_output = ActionHistoryBeautifier.beautify(
    #     model_actions, format='json')
    # markdown_output = ActionHistoryBeautifier.beautify(
    #     model_actions, format='markdown')
    # html_output = ActionHistoryBeautifier.beautify(
    #     model_actions, format='html')

    # # Save the outputs to files
    # with open('action_history.json', 'w', encoding='utf-8') as f:
    #     f.write(json_output)

    # with open('action_history.md', 'w', encoding='utf-8') as f:
    #     f.write(markdown_output)

    # with open('action_history.html', 'w', encoding='utf-8') as f:
    #     f.write(html_output)

    # # Print a summary to console
    # print("\n=== Action History Summary ===")
    # for i, action in enumerate(model_actions):
    #     action_type = next((k for k in action.keys() if k !=
    #                        'interacted_element'), 'unknown')
    #     element = action.get('interacted_element')
    #     tag_name = getattr(element, 'tag_name', 'None') if element else 'None'
    #     print(f"{i+1}. {action_type} - Element: {tag_name}")

    # # Process the final result
    # result = history.final_result()

    # print("\nAction history files generated:")
    # print("- action_history.json")
    # print("- action_history.md")
    # print("- action_history.html")

    # await browser.close()
    input("Press Enter to close the browser")


if __name__ == '__main__':
    asyncio.run(main())
