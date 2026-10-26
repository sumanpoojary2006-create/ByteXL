# Unit 8: Clean Code, Refactoring & Software Evolution

Learn how to write code that others can read, improve it safely, and keep it healthy over years: readable code, naming, functions, comments, formatting and standards, error handling, code smells, refactoring and its common techniques, technical debt, legacy code, why software changes and what it costs, change impact analysis, reverse engineering and program comprehension, modernisation, reuse, documentation, configuration and release management, and end of life and sustainability. Conceptual and theory-focused: no code examples. Source of truth: `Course_Blueprint_for_Software_Engineering.xlsx`, sheet `Syllabus`, Unit 8.

4 chapters, 20 topics.

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
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">8.1 - Writing Readable Code</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">1</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;"><a href="8.1%20-%20Writing%20Readable%20Code/01_what_makes_code_readable.md">What Makes Code Readable?</a></td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">8.1 - Writing Readable Code</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">2</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;"><a href="8.1%20-%20Writing%20Readable%20Code/02_naming_things_well.md">Naming Things Well</a></td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">8.1 - Writing Readable Code</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">3</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;"><a href="8.1%20-%20Writing%20Readable%20Code/03_functions_and_methods_done_right.md">Functions and Methods Done Right</a></td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">8.1 - Writing Readable Code</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">4</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;"><a href="8.1%20-%20Writing%20Readable%20Code/04_comments_and_self_documenting_code.md">Comments and Self-Documenting Code</a></td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">8.1 - Writing Readable Code</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">5</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;"><a href="8.1%20-%20Writing%20Readable%20Code/05_formatting_and_coding_standards.md">Formatting and Coding Standards</a></td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">8.2 - Robust Code and Improving Design</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">6</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;"><a href="8.2%20-%20Robust%20Code%20and%20Improving%20Design/06_error_handling_and_defensive_programming.md">Error Handling and Defensive Programming</a></td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">8.2 - Robust Code and Improving Design</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">7</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;"><a href="8.2%20-%20Robust%20Code%20and%20Improving%20Design/07_code_smells.md">Code Smells</a></td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">8.2 - Robust Code and Improving Design</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">8</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;"><a href="8.2%20-%20Robust%20Code%20and%20Improving%20Design/08_refactoring_fundamentals.md">Refactoring Fundamentals</a></td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">8.2 - Robust Code and Improving Design</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">9</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;"><a href="8.2%20-%20Robust%20Code%20and%20Improving%20Design/09_common_refactorings.md">Common Refactorings</a></td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">8.2 - Robust Code and Improving Design</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">10</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;"><a href="8.2%20-%20Robust%20Code%20and%20Improving%20Design/10_technical_debt.md">Technical Debt</a></td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">8.2 - Robust Code and Improving Design</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">11</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;"><a href="8.2%20-%20Robust%20Code%20and%20Improving%20Design/11_working_with_legacy_code.md">Working with Legacy Code</a></td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">8.3 - Software Evolution and Maintenance</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">12</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;"><a href="8.3%20-%20Software%20Evolution%20and%20Maintenance/12_why_software_changes.md">Why Software Changes</a></td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">8.3 - Software Evolution and Maintenance</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">13</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;"><a href="8.3%20-%20Software%20Evolution%20and%20Maintenance/13_the_cost_of_maintenance.md">The Cost of Maintenance</a></td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">8.3 - Software Evolution and Maintenance</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">14</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;"><a href="8.3%20-%20Software%20Evolution%20and%20Maintenance/14_change_impact_analysis.md">Change Impact Analysis</a></td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">8.3 - Software Evolution and Maintenance</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">15</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;"><a href="8.3%20-%20Software%20Evolution%20and%20Maintenance/15_reverse_engineering_and_program_comprehension.md">Reverse Engineering and Program Comprehension</a></td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">8.4 - Modernisation, Reuse and Lifecycle Management</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">16</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;"><a href="8.4%20-%20Modernisation%2C%20Reuse%20and%20Lifecycle%20Management/16_reengineering_and_modernization.md">Reengineering and Modernization</a></td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">8.4 - Modernisation, Reuse and Lifecycle Management</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">17</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;"><a href="8.4%20-%20Modernisation%2C%20Reuse%20and%20Lifecycle%20Management/17_software_reuse.md">Software Reuse</a></td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">8.4 - Modernisation, Reuse and Lifecycle Management</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">18</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;"><a href="8.4%20-%20Modernisation%2C%20Reuse%20and%20Lifecycle%20Management/18_software_documentation.md">Software Documentation</a></td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">8.4 - Modernisation, Reuse and Lifecycle Management</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">19</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;"><a href="8.4%20-%20Modernisation%2C%20Reuse%20and%20Lifecycle%20Management/19_configuration_management_and_release_management.md">Configuration Management and Release Management</a></td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">8.4 - Modernisation, Reuse and Lifecycle Management</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">20</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;"><a href="8.4%20-%20Modernisation%2C%20Reuse%20and%20Lifecycle%20Management/20_end_of_life_and_software_sustainability.md">End of Life and Software Sustainability</a></td>
    </tr>
  </tbody>
</table>
