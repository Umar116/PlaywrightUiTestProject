import logging
from playwright.sync_api import Locator

logger = logging.getLogger(__name__)


def fill(locator: Locator, value: str, field_name: str = ""):
    logger.info(f" Заполняем поле {field_name or locator} значением: {value}")
    locator.fill(value)


def click(locator: Locator, description: str = ""):
    logger.info(f"Кликаем по: {description or locator}")
    locator.click()


def submit(locator: Locator, description: str = ""):
    logger.info(f"Сабмитим: {description or locator}")
    locator.press("Enter")
