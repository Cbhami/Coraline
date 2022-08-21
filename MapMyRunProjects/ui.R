# Import the library
library(shiny)

# Create UI
shinyUI(
  fluidPage(
    # TASK 1: Application title
    titlePanel(...),
    # Define vertical layout
    verticalLayout(
      # TASK 2: Add plot output
      plotOutput(...),
      # TASK 3: Add slider input
      sliderInput(...)
    )
  )
)
