Feature: Feature Demo
"""
En Scenario: Se indica el concepto de la prueba.
Given: requisitos para ejecutar la prueba.
When: Primer paso para ejecutar la prueba.
And: Segundo paso, etc.
Then: Resultado esperado.
"""
Scenario: login successful
   Given el usuario está registrado
   When cuando introduce un nombre de usuario
   And cuando introduce su password
   And el usuario pulsa el botón de "Login"
   Then el usuario accede al portal