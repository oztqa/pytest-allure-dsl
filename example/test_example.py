# -*- coding: utf-8 -*-

"""
feature: module level feature
"""
import allure


@allure.feature('usual feature.')
def test_example_1(allure_dsl):
    """
    story: story for example
    description: description for example
    attachments:
        - title: json data
          file: attachments/example.json
    steps:
        1: Hello World!
        activity: living in the world!
        2: Cook {dish} and fry {second_dish}
        3: Long good bye
        3-1: bye-bye!
    """
    with allure_dsl.step(1):
        pass

    with allure_dsl.step('activity'):
        pass

    with allure_dsl.step(2, dish='soup', second_dish='sausages'):
        pass

    with allure_dsl.step(3):
        with allure_dsl.step('3-1'):
            pass


def test_example_2():
    """
    feature: function level feature
    story: story for example
    """
    pass


def test_example_3():
    """
    feature: function level feature
    story: story for example
    issue:
        - issue1
        - issue2
    """
    pass


class TestExample:
    """
    feature: class level feature
    """

    def test_example(self):
        """
        story: story for example
        description: description for example
        attachments:
            - title: request
              type: json
              content: '{"hello": "world"}'
        """
        pass
