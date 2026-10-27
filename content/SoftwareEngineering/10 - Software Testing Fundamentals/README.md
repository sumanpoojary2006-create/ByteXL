# Unit 10: Software Testing Fundamentals

Learn why and how software is tested: the purpose and limits of testing, terminology and the test pyramid, unit testing, systematic test design (equivalence partitioning, boundary values, decision tables, state-based testing), white-box testing and code coverage, test doubles, test-driven and behaviour-driven development, integration and system testing, regression testing and automation, acceptance, exploratory, and usability testing, non-functional testing, systematic debugging, and writing good bug reports. Conceptual and theory-focused: no code examples. Source of truth: `Course_Blueprint_for_Software_Engineering.xlsx`, sheet `Syllabus`, Unit 10.

5 chapters, 15 topics.

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
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">10.1 - Testing Foundations</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">1</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;"><a href="10.1%20-%20Testing%20Foundations/01_why_test_software.md">Why Test Software?</a></td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">10.1 - Testing Foundations</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">2</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;"><a href="10.1%20-%20Testing%20Foundations/02_testing_terminology_and_the_test_pyramid.md">Testing Terminology and the Test Pyramid</a></td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">10.1 - Testing Foundations</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">3</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;"><a href="10.1%20-%20Testing%20Foundations/03_unit_testing.md">Unit Testing</a></td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">10.2 - Test Design Techniques</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">4</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;"><a href="10.2%20-%20Test%20Design%20Techniques/04_test_design_equivalence_partitioning_and_boundary_value_analysis.md">Test Design: Equivalence Partitioning and Boundary Value Analysis</a></td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">10.2 - Test Design Techniques</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">5</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;"><a href="10.2%20-%20Test%20Design%20Techniques/05_test_design_decision_tables_and_state_based_testing.md">Test Design: Decision Tables and State-Based Testing</a></td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">10.2 - Test Design Techniques</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">6</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;"><a href="10.2%20-%20Test%20Design%20Techniques/06_white_box_testing_and_code_coverage.md">White-Box Testing and Code Coverage</a></td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">10.3 - Testing Practices for Better Design</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">7</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;"><a href="10.3%20-%20Testing%20Practices%20for%20Better%20Design/07_test_doubles_stubs_mocks_and_fakes.md">Test Doubles: Stubs, Mocks and Fakes</a></td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">10.3 - Testing Practices for Better Design</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">8</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;"><a href="10.3%20-%20Testing%20Practices%20for%20Better%20Design/08_test_driven_development.md">Test-Driven Development</a></td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">10.3 - Testing Practices for Better Design</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">9</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;"><a href="10.3%20-%20Testing%20Practices%20for%20Better%20Design/09_behaviour_driven_development.md">Behaviour-Driven Development</a></td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">10.4 - Testing at Higher Levels</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">10</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;"><a href="10.4%20-%20Testing%20at%20Higher%20Levels/10_integration_and_system_testing.md">Integration and System Testing</a></td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">10.4 - Testing at Higher Levels</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">11</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;"><a href="10.4%20-%20Testing%20at%20Higher%20Levels/11_regression_testing_and_test_automation.md">Regression Testing and Test Automation</a></td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">10.4 - Testing at Higher Levels</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">12</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;"><a href="10.4%20-%20Testing%20at%20Higher%20Levels/12_acceptance_exploratory_and_usability_testing.md">Acceptance, Exploratory and Usability Testing</a></td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">10.4 - Testing at Higher Levels</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">13</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;"><a href="10.4%20-%20Testing%20at%20Higher%20Levels/13_non_functional_testing.md">Non-Functional Testing</a></td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">10.5 - Finding and Reporting Defects</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">14</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;"><a href="10.5%20-%20Finding%20and%20Reporting%20Defects/14_debugging_systematically.md">Debugging Systematically</a></td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">10.5 - Finding and Reporting Defects</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">15</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;"><a href="10.5%20-%20Finding%20and%20Reporting%20Defects/15_writing_good_bug_reports.md">Writing Good Bug Reports</a></td>
    </tr>
  </tbody>
</table>
