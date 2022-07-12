Feature: BigBasket product order
  Scenario: Product Order
    Given Lunch chrome browser
    When Open Big Basket website
    And Select city and  continue
    Given Scroll to Best sellers area
    When Adding product to kart
    Then Assert Add button
    Then Assert My Basket title updated
    When Hover on My Basket
    Then Assert same product selected
    When click on View Basket and Checkout
    Then Assert Login popup is display
    When Taking screenshot
    Then close popup and close drive
