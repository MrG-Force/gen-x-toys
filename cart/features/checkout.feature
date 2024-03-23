Feature: Checkout Process: Billing Form Interactions
  In order to ensure a smooth and error-free checkout process
  As a visitor to GenXToys
  I want to fill out, review, and edit my billing information with clear feedback and validation

  Scenario: Fill out the billing form
    Given a visitor to GenXToys has arrived at the checkout page
    And the billing form is visible
    And the 'Next' button in the billing form is initially disabled
    When they correctly fill out all required fields in the billing form
    Then the 'Next' button should become enabled

  Scenario: Transition from billing to shipping form
    Given a visitor to GenXToys has completed the billing form
    When they click the 'Next' button
    Then the billing form should collapse
    And the shipping form should expand

  Scenario: Review the billing information
    Given a visitor to GenXToys has completed the billing form
    And they have clicked the 'Next' button
    When they choose to expand the billing form for review
    Then the input fields in the billing form should be read-only
    And the 'Next' button should have morphed into an 'Edit' button

  Scenario: Allow user to make the billing form editable again
    Given a visitor to GenXToys has reviewed their completed billing form
    And the billing form is in a read-only state with an 'Edit' button present
    When the user clicks the 'Edit' button
    Then the billing form should become editable
    And the 'Edit' button should morph back into a 'Next' button
