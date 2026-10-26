## Introduction

User-facing applications face a recurring problem: the same information must be shown in several ways, the user can change it through several routes, and the business rules should not be tangled with screen layout. If these concerns are mixed together, any change to the interface risks the rules, and any change to the rules breaks the interface. The Model-View-Controller pattern, and the family of variants that followed it, separates these concerns and is among the most widely used structures in application development.

**Definition:** Model-View-Controller (MVC) is an architectural pattern that separates an application into a model, which holds the data and business rules, a view, which presents information to the user, and a controller, which handles user input and coordinates the other two, so that each can change independently.

<!--
IMAGE PROMPT  ->  generate as images/05_intro_model_view_controller_and_its_variants.png   (16:9 cinematic hero image, place here, right after the Introduction)

CHARACTER & THEME: Software Engineering course introduction image based directly on the opening scene of this lesson. Show the core idea of the lesson visually, with no named characters.

STYLE: world-class high-end 3D render, cinematic and vibrant, glossy soft 3D forms, blue software forms, green positive accents, orange secondary accents, red warnings, soft studio-gradient backdrop, minimal large labels.

SCENE: A triangle with three labelled nodes Model, View, Controller, arrows showing the user acting on the Controller, the Controller updating the Model, and the Model notifying the View, which shows output to the user.

ON-IMAGE TEXT: show a short bold title "Model View Controller and Its Variants" plus only these few labels, large and legible: Model, View, Controller. Keep text minimal, no sentences.

GOAL: make the opening idea instantly clear and engaging while matching the existing reading-material image standards.
-->

## Origins

Trygve Reenskaug devised MVC in 1979 while working at Xerox PARC, and it became a core idea of the Smalltalk environment. It was created to bridge the gap between the way a user thinks about information and the way it is stored in a computer. Since then it has been adapted to desktop, web, and mobile development.

## The Three Roles

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Role</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Responsibility</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Knows about</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Example in an ordering app</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Model</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Holds the data and the business rules; notifies others when it changes</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Nothing about the view or controller</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">The Order, with its items, total, and rules for changes</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">View</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Presents the model to the user; may show the same model in several ways</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">The model, in order to display it</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">An order summary screen, or a kitchen display of the same orders</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Controller</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Receives user input, interprets it, and tells the model or view what to do</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Both the model and the view</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Handles a tap on "Add to basket" by asking the Order to add the item</td>
    </tr>
  </tbody>
</table>

## How They Interact

1. The user acts on the interface, for example pressing a button.
2. The controller receives the action and translates it into a request to the model.
3. The model changes its state, applying business rules.
4. The model signals that it has changed, directly or through the controller.
5. The view obtains the new state and updates what the user sees.

The key point is that the **model does not depend on the view or controller**. It can be tested without any interface, and several different views can present the same model at once.

## Why It Helps

- **Separation of concerns:** interface changes do not disturb business rules.
- **Multiple views:** the same data can appear as a list, a chart, or on another device.
- **Parallel work:** interface designers and logic developers can work independently.
- **Testability:** the model and the controller logic can be tested without a screen.
- **Reuse:** a model can serve different interfaces, such as web and mobile.

## Variants

The original arrangement has been adapted to suit different technologies. The most common variants differ in how the view and the logic around it are connected.

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Pattern</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Structure</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Key difference</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Typical setting</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">MVC (web style)</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Controller receives each request, uses the model, and selects a view to produce the response</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Controller is the entry point for every request; the view is typically rendered by the server</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Server-side web frameworks</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">MVP (Model-View-Presenter)</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">The presenter takes over the logic of the controller and updates a passive view</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">The view is passive and knows nothing about the model; very testable</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Desktop and some mobile interfaces</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">MVVM (Model-View-ViewModel)</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A view model exposes data and commands in a form ready for display; the view binds to it automatically</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Data binding keeps the view and view model synchronised with little code</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Rich client frameworks, modern mobile and web applications</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Unidirectional flow patterns</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">State is kept in one store, actions change it, and views render from it</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Data flows in one direction, making changes predictable</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Complex single-page web applications</td>
    </tr>
  </tbody>
</table>

## Common Pitfalls

- **Fat controllers:** business logic creeps into the controller, which becomes large and hard to test. Rules belong in the model.
- **Anaemic models:** the model holds only data, and all behaviour lives elsewhere, so the model enforces no rules.
- **Logic in the view:** decisions embedded in templates or screens are hard to test and reuse.
- **Over-notification:** too many fine-grained updates cause flicker and unpredictable behaviour.
- **Misusing the name:** many frameworks use the term MVC loosely, so the actual responsibilities should be checked.

## MVC and Layered Architecture

MVC organises the user-facing part of an application, and it fits inside a layered or three-tier system. For example, the presentation layer may use MVC, while the model delegates to domain and data layers beneath it. The two ideas are complementary.

<!--
IMAGE PROMPT  ->  generate as images/02_mvc_mvp_mvvm_comparison.png   (16:9 explanatory diagram, place here)

Three small triangle or chain diagrams side by side. MVC: user to Controller to Model, Model notifies View. MVP: View passive, Presenter in the middle, Model. MVVM: View bound to ViewModel with a double arrow labelled Data binding, ViewModel to Model.

STYLE: clean flat-3D infographic, blue primary forms, green for correct or healthy, orange for caution, red for failure, large legible labels, minimal text.
-->

## Your Turn: Assign the Role

1. The rule that an order cannot be changed once preparation starts.
2. The screen that lists the items in an order.
3. The code that receives a tap on "Cancel order" and asks for the change.

Item 1 belongs in the model, since it is a business rule. Item 2 is the view. Item 3 is the controller, or the presenter or view model in a variant.

## Conclusion

Model-View-Controller (MVC) is an architectural pattern that separates an application into a model, which holds the data and business rules, a view, which presents information to the user, and a controller, which handles user input and coordinates the other two, so that each can change independently. Its variants adapt the same separation to different technologies.

MVC arranges the parts inside one application. The next topic considers the extreme of keeping everything together as one unit: the monolith.
