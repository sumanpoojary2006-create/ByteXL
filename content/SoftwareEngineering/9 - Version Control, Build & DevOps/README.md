# Unit 9: Version Control, Build & DevOps

Learn the tools and practices that make the daily work of changing software safe, collaborative, and repeatable: why version control matters and how Git works, commits, branching and merging, merge conflicts, remote collaboration, branching strategies, pull requests and code review, rewriting history, tags and semantic versioning, issue tracking, open-source collaboration, builds and dependency management, continuous integration and delivery, environments and configuration, containers, infrastructure as code, release strategies, monitoring and observability, incident response and postmortems, and the DevOps culture. Conceptual and theory-focused: no code examples (Git operation names appear only as vocabulary). Source of truth: `Course_Blueprint_for_Software_Engineering.xlsx`, sheet `Syllabus`, Unit 9.

6 chapters, 23 topics.

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
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">9.1 - Version Control Foundations</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">1</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;"><a href="9.1%20-%20Version%20Control%20Foundations/01_why_version_control.md">Why Version Control?</a></td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">9.1 - Version Control Foundations</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">2</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;"><a href="9.1%20-%20Version%20Control%20Foundations/02_git_fundamentals.md">Git Fundamentals</a></td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">9.1 - Version Control Foundations</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">3</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;"><a href="9.1%20-%20Version%20Control%20Foundations/03_commits_history_and_good_commit_messages.md">Commits, History and Good Commit Messages</a></td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">9.1 - Version Control Foundations</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">4</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;"><a href="9.1%20-%20Version%20Control%20Foundations/04_branching_and_merging.md">Branching and Merging</a></td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">9.1 - Version Control Foundations</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">5</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;"><a href="9.1%20-%20Version%20Control%20Foundations/05_resolving_merge_conflicts.md">Resolving Merge Conflicts</a></td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">9.2 - Collaborating with Git</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">6</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;"><a href="9.2%20-%20Collaborating%20with%20Git/06_remote_repositories_and_collaboration.md">Remote Repositories and Collaboration</a></td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">9.2 - Collaborating with Git</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">7</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;"><a href="9.2%20-%20Collaborating%20with%20Git/07_branching_strategies.md">Branching Strategies</a></td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">9.2 - Collaborating with Git</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">8</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;"><a href="9.2%20-%20Collaborating%20with%20Git/08_pull_requests_and_the_code_review_workflow.md">Pull Requests and Code Review Workflow</a></td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">9.2 - Collaborating with Git</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">9</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;"><a href="9.2%20-%20Collaborating%20with%20Git/09_rebasing_cherry_picking_and_rewriting_history.md">Rebasing, Cherry-Picking and Rewriting History</a></td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">9.3 - Releases, Planning and Open-Source Collaboration</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">10</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;"><a href="9.3%20-%20Releases%2C%20Planning%20and%20Open-Source%20Collaboration/10_tags_releases_and_semantic_versioning.md">Tags, Releases and Semantic Versioning</a></td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">9.3 - Releases, Planning and Open-Source Collaboration</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">11</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;"><a href="9.3%20-%20Releases%2C%20Planning%20and%20Open-Source%20Collaboration/11_issue_tracking_and_project_boards.md">Issue Tracking and Project Boards</a></td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">9.3 - Releases, Planning and Open-Source Collaboration</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">12</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;"><a href="9.3%20-%20Releases%2C%20Planning%20and%20Open-Source%20Collaboration/12_open_source_collaboration.md">Open-Source Collaboration</a></td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">9.4 - Building and Delivering Software</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">13</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;"><a href="9.4%20-%20Building%20and%20Delivering%20Software/13_from_source_code_to_deployable_software.md">From Source Code to Deployable Software</a></td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">9.4 - Building and Delivering Software</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">14</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;"><a href="9.4%20-%20Building%20and%20Delivering%20Software/14_build_tools_and_dependency_management.md">Build Tools and Dependency Management</a></td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">9.4 - Building and Delivering Software</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">15</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;"><a href="9.4%20-%20Building%20and%20Delivering%20Software/15_continuous_integration.md">Continuous Integration</a></td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">9.4 - Building and Delivering Software</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">16</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;"><a href="9.4%20-%20Building%20and%20Delivering%20Software/16_continuous_delivery_and_deployment.md">Continuous Delivery and Deployment</a></td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">9.5 - Environments, Containers and Releases</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">17</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;"><a href="9.5%20-%20Environments%2C%20Containers%20and%20Releases/17_environments_and_configuration_management.md">Environments and Configuration Management</a></td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">9.5 - Environments, Containers and Releases</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">18</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;"><a href="9.5%20-%20Environments%2C%20Containers%20and%20Releases/18_containers_for_developers.md">Containers for Developers</a></td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">9.5 - Environments, Containers and Releases</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">19</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;"><a href="9.5%20-%20Environments%2C%20Containers%20and%20Releases/19_infrastructure_as_code.md">Infrastructure as Code</a></td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">9.5 - Environments, Containers and Releases</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">20</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;"><a href="9.5%20-%20Environments%2C%20Containers%20and%20Releases/20_release_strategies.md">Release Strategies</a></td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">9.6 - Operating Software and DevOps Culture</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">21</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;"><a href="9.6%20-%20Operating%20Software%20and%20DevOps%20Culture/21_monitoring_logging_and_observability.md">Monitoring, Logging and Observability</a></td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">9.6 - Operating Software and DevOps Culture</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">22</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;"><a href="9.6%20-%20Operating%20Software%20and%20DevOps%20Culture/22_incident_response_and_postmortems.md">Incident Response and Postmortems</a></td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">9.6 - Operating Software and DevOps Culture</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">23</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;"><a href="9.6%20-%20Operating%20Software%20and%20DevOps%20Culture/23_the_devops_culture.md">The DevOps Culture</a></td>
    </tr>
  </tbody>
</table>
