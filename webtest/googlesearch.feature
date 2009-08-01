Scenario: Search for Hello World with google
    Given I open http://www.google.com
    When I search for "Hello World"
    Then I expect to find a link to http://en.wikipedia.org/wiki/Hello_world_program