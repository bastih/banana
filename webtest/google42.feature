Scenario: Search for Hello World with google
    Given I open http://www.google.com
    When I search for "The answer to life, the universe and everything"
    Then I expect to see 42