## Introduction

Many designs need one object to notify others when something happens. When an order changes status, the customer screen must update, the kitchen display must refresh, and an analytics record must be written. If the order object calls each of these directly, it becomes tied to all of them, and every new interested party means editing the order. The Observer pattern solves this by letting interested parties register themselves, so that the source knows only that there are some listeners and nothing about who they are.

**Definition:** The Observer pattern defines a one-to-many dependency between objects so that when one object, the subject, changes state, all its registered dependents, the observers, are notified automatically, without the subject needing to know their concrete types.

<!--
IMAGE PROMPT  ->  generate as images/09_intro_the_observer_pattern_and_event_handling.png   (16:9 cinematic hero image, place here, right after the Introduction)

CHARACTER & THEME: Software Engineering course introduction image based on the central concept of this lesson. Show the core idea of the lesson visually, with no named characters.

STYLE: world-class high-end 3D render, cinematic and vibrant, glossy soft 3D forms, blue software forms, green positive accents, orange secondary accents, red warnings, soft studio-gradient backdrop, minimal large labels.

SCENE: A central broadcasting tower labelled Order status (subject) with signal waves reaching three receivers labelled Customer screen, Kitchen display, Analytics, each of which has a small subscribe button.

ON-IMAGE TEXT: show a short bold title "The Observer Pattern" plus only these few labels, large and legible: Subject, Observers, Notify. Keep text minimal, no sentences.

GOAL: make the opening idea instantly clear and engaging while matching the existing reading-material image standards.
-->

## Roles

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Role</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Responsibility</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Example</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Subject (publisher)</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Holds the state of interest and a list of observers; allows observers to subscribe and unsubscribe; notifies them when its state changes</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Order</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Observer interface</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Declares the operation by which observers are told of a change</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Order Listener: order changed</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Concrete observers</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">React to the change in their own way</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Customer Screen, Kitchen Display, Analytics Recorder</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Client</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Connects observers to subjects</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Application set-up code</td>
    </tr>
  </tbody>
</table>

## How It Works

1. An observer **subscribes** to the subject, giving it a way to be called.
2. The subject's state changes.
3. The subject **notifies** every observer on its list, telling them what changed.
4. Each observer **reacts** independently, for example by updating a display.
5. An observer may **unsubscribe** when it no longer cares.

The subject knows only that each observer implements the observer interface, so it is **loosely coupled** to them. New observers can be added without changing the subject, which follows the open-closed principle.

## Push and Pull

There are two ways to give observers information.

- **Push:** the subject sends the new data with the notification. Observers get what they need immediately, but the subject must guess what each wants, and may send too much.
- **Pull:** the subject sends only a signal that something changed, and observers ask for the details they need. Observers are more independent, but must make further requests.

## Benefits

- **Loose coupling** between the source of events and the parties that care.
- **Dynamic relationships:** observers can come and go at run time.
- **Broadcast communication:** one change reaches many observers.
- **Separation of concerns:** the subject does not contain code for displays, logging, or analytics.

## Pitfalls

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Problem</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Explanation</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Remedy</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Unexpected updates</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A small change cascades through many observers, whose own changes trigger further notifications</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Keep chains short; avoid observers that modify the subject in response</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Memory leaks (lapsed listener)</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">An observer that is no longer needed remains subscribed, so the subject keeps it alive</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Always unsubscribe; use weak references where supported</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Order of notification</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">The order in which observers are called is usually unspecified</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Do not depend on it</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Slow observers</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A slow observer delays the subject and all others when notification is synchronous</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Notify asynchronously, or hand off work to a queue</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Error handling</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A failing observer may prevent others from being notified</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Isolate failures so that one does not block the rest</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Hard to trace</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Control flow is implicit; it is not obvious from the subject who will react</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Document events; use tooling to trace</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Thread safety</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Observers may be added or removed while a notification is in progress</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Take a snapshot of the list before notifying</td>
    </tr>
  </tbody>
</table>

## Observer in the Wider World

The idea appears at every scale.

- In **MVC**, the view observes the model, as Unit 6 described.
- **User interface events**, such as clicks, are delivered to handlers that have registered for them.
- **Publish-subscribe messaging** is the same idea carried across processes and machines, with a broker between publisher and subscribers.
- **Reactive programming** extends it into streams of events that can be filtered, combined, and transformed.
- **Spreadsheets** recalculate dependent cells when a value changes, which is observer behaviour.

The difference between the in-process pattern and a message broker lies in coupling and failure: with a broker, publisher and subscriber are independent in time and place, while a direct observer is called in the same process and at the same moment.

<!--
IMAGE PROMPT  ->  generate as images/02_observer_subscribe_notify.png   (16:9 explanatory diagram, place here)

A sequence of numbered steps: 1 Observers subscribe to the Order, 2 Order status changes to Ready, 3 Order notifies all observers, 4 each observer updates itself. A warning icon shows a forgotten observer still subscribed after its screen has closed, labelled Lapsed listener.

STYLE: clean flat-3D infographic, blue primary forms, green for correct or healthy, orange for caution, red for failure, large legible labels, minimal text.
-->

## Your Turn: Spot the Issue

1. A closed screen is still receiving updates, and its memory is never released. What is the cause?
2. A subject notifies its observers, and one observer changes the subject, which triggers another notification, and so on without end. What has gone wrong?
3. Why does the Observer pattern let a new analytics recorder be added without touching the Order code?

The first is a lapsed listener: the observer forgot to unsubscribe. The second is a notification cascade, where an observer modifies the subject in response to a notification, creating a loop. In the third, the Order only knows that it notifies any observers that implement the interface, so a new observer needs only to subscribe.

## Conclusion

The Observer pattern defines a one-to-many dependency between objects so that when one object, the subject, changes state, all its registered dependents, the observers, are notified automatically, without the subject needing to know their concrete types. It underlies event handling, user interfaces, and messaging, and requires care with subscriptions and cascades.

Three further behavioural patterns solve common structuring problems of requests, algorithms, and traversal. The next topic describes Command, Template Method, and Iterator.
