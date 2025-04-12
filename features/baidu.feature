Feature: 百度搜索
  Scenario: 搜索关键词
    Given 关键词 behave
    When 打开百度页面
    And  输入关键词
    And  点击百度一下按钮
    Then 页面标题中应包含关键词
