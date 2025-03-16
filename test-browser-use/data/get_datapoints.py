example_test_steps = """
1. Search for Machine Learning
2. Choose the first link
"""


"""
Keep human in the loop to verify the results.

Objectives
- Nghĩ ra metrics để xác thực rằng kết quả code sinh ra từ AI là đủ (vd: độ coverage, happy cases, edge cases)
- Nghĩ về độ xác thực.
- Metrics có thể lấy từ QEs, khảo sát.
- Verify the verifiers ***
- Vận dụng các Agents có sẵn trên thị trường để tạo kết quả, không cố gắng đào sâu về Agents (xài tụi nó như blackbox) --> Dựa trên các metrics (chưa nghĩ ra), ta sẽ:
    - So sánh kết quả giữa Agent - Human, Agent - Agent.
    - Đề xuất process chuẩn hoá quá trình viết tests nhờ Agent.

"""