# Unit 6: Software Architecture

Learn how the major structure of a software system is chosen and judged: what architecture is, how quality attributes drive it, the main architectural styles (layered, client-server and three-tier, MVC, monolithic, microservices, event-driven, pipes and filters), the fundamentals of distributed systems, how architecture is documented, and how trade-offs are evaluated. Conceptual and theory-focused: no code examples. Source of truth: `Course_Blueprint_for_Software_Engineering.xlsx`, sheet `Syllabus`, Unit 6.

3 chapters, 12 topics.

## Topics

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Chapter</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Topic #</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Topic</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">6.1 - Architecture Foundations</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">1</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;"><a href="6.1%20-%20Architecture%20Foundations/01_what_is_software_architecture.md">What Is Software Architecture?</a></td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">6.1 - Architecture Foundations</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">2</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;"><a href="6.1%20-%20Architecture%20Foundations/02_architectural_drivers_and_quality_attributes.md">Architectural Drivers and Quality Attributes</a></td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">6.1 - Architecture Foundations</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">3</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;"><a href="6.1%20-%20Architecture%20Foundations/03_layered_architecture.md">Layered Architecture</a></td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">6.1 - Architecture Foundations</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">4</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;"><a href="6.1%20-%20Architecture%20Foundations/04_client_server_and_three_tier_systems.md">Client-Server and Three-Tier Systems</a></td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">6.2 - Architectural Styles</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">5</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;"><a href="6.2%20-%20Architectural%20Styles/05_model_view_controller_and_its_variants.md">Model-View-Controller and Its Variants</a></td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">6.2 - Architectural Styles</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">6</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;"><a href="6.2%20-%20Architectural%20Styles/06_monolithic_architecture.md">Monolithic Architecture</a></td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">6.2 - Architectural Styles</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">7</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;"><a href="6.2%20-%20Architectural%20Styles/07_microservices_architecture.md">Microservices Architecture</a></td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">6.2 - Architectural Styles</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">8</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;"><a href="6.2%20-%20Architectural%20Styles/08_event_driven_and_message_based_architecture.md">Event-Driven and Message-Based Architecture</a></td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">6.2 - Architectural Styles</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">9</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;"><a href="6.2%20-%20Architectural%20Styles/09_pipes_and_filters_and_data_flow_architectures.md">Pipes-and-Filters and Data-Flow Architectures</a></td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">6.3 - Distribution, Documentation and Evaluation</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">10</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;"><a href="6.3%20-%20Distribution%2C%20Documentation%20and%20Evaluation/10_distributed_system_fundamentals_for_engineers.md">Distributed System Fundamentals for Engineers</a></td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">6.3 - Distribution, Documentation and Evaluation</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">11</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;"><a href="6.3%20-%20Distribution%2C%20Documentation%20and%20Evaluation/11_documenting_architecture.md">Documenting Architecture</a></td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">6.3 - Distribution, Documentation and Evaluation</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">12</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;"><a href="6.3%20-%20Distribution%2C%20Documentation%20and%20Evaluation/12_evaluating_architecture_trade_offs.md">Evaluating Architecture Trade-offs</a></td>
    </tr>
  </tbody>
</table>
