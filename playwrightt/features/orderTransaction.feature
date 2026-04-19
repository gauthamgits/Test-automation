Feature: Order Transaction


  Scenario Outline: Verify Order success message is shown in details page
    Given the user has placed an order with <username> and <password>
    And the user is on landing page
    When i login to the portal with <username> and <password>
    And navigate to the orders page
    And select the orderid
    Then order message is successfully displayed
    Examples:
      | username              | password    |
      | rahulshetty@gmail.com | Iamking@000 |

