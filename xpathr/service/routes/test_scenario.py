from flask import Blueprint, jsonify, request
from ..error_handler import BadRequestError, NotFoundError

test_scenario_bp = Blueprint('test_scenarios', __name__)

example_scenarios = [
    {
        "id": 1,
        "website_url": "https://example.com",
        "test_objective": "Verify login functionality",
        "description": "Test the login functionality with valid credentials.",
        "precondition": "User must have a valid account.",
        "capture_screenshots": True
    },
    {
        "id": 2,
        "website_url": "https://example.com",
        "test_objective": "Check page title",
        "description": "Ensure the page title is correct.",
        "precondition": "",
        "capture_screenshots": False
    }
]


@test_scenario_bp.route('/', methods=['GET'])
def get_test_scenarios():
    return jsonify({"test_scenarios": example_scenarios})


@test_scenario_bp.route('/<int:scenario_id>', methods=['GET'])
def get_test_scenario(scenario_id):
    scenario = next(
        (scenario for scenario in example_scenarios if scenario["id"] == scenario_id), None)
    if not scenario:
        raise NotFoundError(f"Test scenario with ID {scenario_id} not found")
    return jsonify(scenario)


@test_scenario_bp.route('/', methods=['POST'])
def create_test_scenario():
    """Create a new test scenario"""
    data = request.get_json()

    required_fields = ['website_url', 'test_objective']
    if not data or not all(field in data for field in required_fields):
        raise BadRequestError(
            f"Missing required fields: {', '.join(required_fields)}")

    new_scenario = {
        "id": len(test_scenarios) + 1,
        "website_url": data["website_url"],
        "test_objective": data["test_objective"],
        "description": data.get("description", ""),
        "precondition": data.get("precondition", ""),
        "capture_screenshots": data.get("capture_screenshots", False)
    }

    test_scenarios.append(new_scenario)
    return jsonify(new_scenario), 201


# @test_scenario_bp.route('/<int:scenario_id>', methods=['PUT'])
# def update_test_scenario(scenario_id):
#     """Update an existing test scenario"""
#     data = request.get_json()

#     # Find the scenario
#     scenario_index = next((i for i, scenario in enumerate(test_scenarios)
#                           if scenario["id"] == scenario_id), None)

#     if scenario_index is None:
#         raise NotFoundError(f"Test scenario with ID {scenario_id} not found")

#     # Update fields that are present in the request
#     for key in ['website_url', 'test_objective', 'description', 'precondition', 'capture_screenshots']:
#         if key in data:
#             test_scenarios[scenario_index][key] = data[key]

#     return jsonify(test_scenarios[scenario_index])


# @test_scenario_bp.route('/<int:scenario_id>', methods=['DELETE'])
# def delete_test_scenario(scenario_id):
#     """Delete a test scenario"""
#     scenario_index = next((i for i, scenario in enumerate(test_scenarios)
#                           if scenario["id"] == scenario_id), None)

#     if scenario_index is None:
#         raise NotFoundError(f"Test scenario with ID {scenario_id} not found")

#     # Remove the scenario
#     deleted_scenario = test_scenarios.pop(scenario_index)

#     return jsonify({
#         "message": f"Test scenario with ID {scenario_id} has been deleted",
#         "deleted_scenario": deleted_scenario
#     })
