import asyncio
from browser_use import Browser, BrowserConfig, Controller, Agent
from llm import llm
from data.instructions import example_test_steps
from pydantic import BaseModel
from typing import List
import json


class Post(BaseModel):
    video_title: str
    video_url: str
    video_creator: str
    views: int
    xpath: str
    id: str


class Posts(BaseModel):
    posts: List[Post]


controller = Controller(output_model=Posts)


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


async def main():
    history = await agent.run()

    result = history.final_result()
    model_actions = history.model_actions()
    posts_data = []
    if result:
        parsed: Posts = Posts.model_validate_json(result)

        posts_data.append(parsed.dict())
        for post in parsed.posts:
            print('\n--------------------------------')
            print(f'Title:            {post.video_title}')
            print(f'URL:              {post.video_url}')
            print(f'Views:         {post.views}')
            print(f'Creator: {post.video_creator}')
            print(f'Xpath: {post.xpath}')
            print(f'Id: {post.id}')
            print('--------------------------------\n')
            print(f'[actions]: {format(model_actions)}')

        with open('results.json', 'w') as json_file:
            json.dump(posts_data, json_file, indent=4)
    else:
        print('No result')

    await browser.close()
    input("Press Enter to close the browser")

if __name__ == '__main__':
    asyncio.run(main())
