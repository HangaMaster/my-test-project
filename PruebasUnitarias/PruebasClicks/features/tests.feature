Feature: Plan de pruebas

  Scenario: Primer boton
    Given navegar a la url
    When pulsar en el primer boton
    When pulsar en aceptar
    Then comprobar que se ha aceptado

  Scenario: Segundo boton
    Given navegar a la url
    When pulsar en el segundo boton
    When pulsar en aceptar
    When comprobar que se ha confirmado
    When pulsar en el segundo boton
    When pulsar en cancelar
    Then comprobar que se ha cancelado
  @wip
  Scenario Outline: Tercer boton
    Given navegar a la url
    When pulsar en el tercer boton
    When introducir el texto '<texto>'
    Then comprobar que el texto pone '<texto>'

    Examples:
      | texto     |
      | Pruebas   |
      | 123213211 |
      | $%(-!&_:  |