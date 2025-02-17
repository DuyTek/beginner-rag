import asyncio
from browser_use.browser.browser import Browser, BrowserConfig
from llm import llm
from browser_use import Agent
from data.get_datapoints import example_test_steps


browser = Browser(
    config=BrowserConfig(
        chrome_instance_path='/Applications/Google Chrome.app/Contents/MacOS/Google Chrome',
        headless=False,
        disable_security=True,
    )
)


initial_actions= [
      {
        'open_tab': {'url': 'http://localhost:6006'}
      }
]


agent = Agent(
    task=example_test_steps,
    llm=llm,
    initial_actions=initial_actions,
    browser=browser,
)

async def main():
    await agent.run()
    await browser.close()
    input("Press Enter to close the browser")

if __name__ == '__main__':
	asyncio.run(main())