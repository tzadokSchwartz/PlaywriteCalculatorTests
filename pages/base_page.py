from playwright.sync_api import Page

class BasePage:
    def __init__(self, page: Page):
        self._page = page

    def wait_for_element(self, selector: str):
        try:
            self._page.locator(selector).wait_for(state="visible", timeout=10000)
        except TimeoutError:
            raise Exception(f"Element with selector '{selector}' not found or not visible!")

    def fill(self, selector: str, text: str) -> None:
        self.wait_for_element(selector)
        self.highlight_element(selector)
        self._page.locator(selector).fill(text)

    def click(self, selector: str) -> None:
        self.wait_for_element(selector)
        self.highlight_element(selector)
        self._page.locator(selector).click()

    def select(self, selector: str, value: str) -> None:
        self.wait_for_element(selector)
        self.highlight_element(selector)
        self._page.locator(selector).select_option(value=value)

    def get_text(self, selector: str) -> str:
        self.wait_for_element(selector)
        text = self._page.locator(selector).inner_text()
        return text

    def is_checked(self, selector: str) -> bool:
        self.wait_for_element(selector)
        return self._page.is_checked(selector)

    def is_visible(self, selector: str) -> bool:
        self.wait_for_element(selector)
        return self._page.is_visible(selector)

    def get_url(self) -> str:
        return self._page.url

    def type(self, selector: str, text: str) -> None:
        self.wait_for_element(selector)
        self.highlight_element(selector)
        self._page.locator(selector).type(text, delay=500)

    def highlight_element(self, selector):
        self._page.evaluate(f"""
            const el = document.querySelector("{selector}");
            if (!document.getElementById('highlight-style')) {{
                const style = document.createElement('style');
                style.id = 'highlight-style';
                style.textContent = `
                    .highlight {{
                        box-shadow: 0 0 15px 5px yellow;
                        background-color: yellow;
                        transition: all 0.3s ease-in-out;
                        border-radius: 6px;
                    }}
                `;
                document.head.appendChild(style);
            }}

            if (el) {{
                el.classList.add('highlight');
                setTimeout(() => {{
                    el.classList.remove('highlight');
                }}, 2000);
            }}
        """)

