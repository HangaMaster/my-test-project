Feature: GET and POST
"""
En Scenario: Se indica el concepto de la prueba.
Given: requisitos para ejecutar la prueba.
When: Primer paso para ejecutar la prueba.
And: Segundo paso, etc.
Then: Resultado esperado.
"""
Scenario: GET Method
   Given Launch GET method
   When Check if data is received
   Then Check if sum is correct

   Scenario: POST Method
   Given Launch POST method
   When Check if data is received
   Then Check if sum is correct