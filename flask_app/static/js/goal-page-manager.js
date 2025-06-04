document.querySelectorAll(".goal-accordion-btn").forEach(button => {
  button.addEventListener('change', syncAccordionHeader())
})

function syncAccordionHeader(event) {
const accordionHeader = event.target
const goalName = accordionHeader.closest(".goal-name")
accordionHeader.innerText(goalName)
}