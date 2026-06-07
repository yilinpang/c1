import requests
import json
from typing import Dict, Optional

class CozeAgent:
    def __init__(self, agent_id: str):
        self.agent_id = agent_id
        self.base_url = "https://www.coze.cn/api/v1/chat"
        self.headers = {
            "Content-Type": "application/json",
            "Authorization": "Bearer YOUR_API_KEY"  # 需要替换为实际的 API Key
        }
    
    def chat(self, message: str) -> Optional[Dict]:
        """
        与 Coze 智能体进行对话
        
        Args:
            message: 用户输入的消息
            
        Returns:
            Dict: 智能体的响应
        """
        try:
            payload = {
                "agent_id": self.agent_id,
                "message": message,
                "stream": False
            }
            
            response = requests.post(
                self.base_url,
                headers=self.headers,
                json=payload
            )
            
            if response.status_code == 200:
                return response.json()
            else:
                print(f"请求失败: {response.status_code}")
                print(f"错误信息: {response.text}")
                return None
                
        except Exception as e:
            print(f"发生错误: {str(e)}")
            return None

def main():
    # 创建 CozeAgent 实例
    agent = CozeAgent("7485685236027146278")
    
    # 测试对话
    test_message = "请分析最近关于'人工智能'的舆情"
    response = agent.chat(test_message)
    
    if response:
        print("智能体响应:")
        print(json.dumps(response, ensure_ascii=False, indent=2))
    else:
        print("获取响应失败")

if __name__ == "__main__":
    main() 