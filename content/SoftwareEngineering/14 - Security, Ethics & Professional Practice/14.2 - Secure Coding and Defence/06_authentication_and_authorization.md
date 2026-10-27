## Introduction

Most systems must answer two questions about every request: who is making it, and are they allowed to do it? The first is authentication, proving identity; the second is authorisation, deciding what that identity may do. They are distinct, and confusing them is a common source of serious flaws: a system may be certain who a user is and still let them act on someone else's data. Both are among the hardest parts of an application to get right, which is why engineers are advised to use established standards and services rather than invent their own.

This topic explains authentication factors and password handling, multi-factor authentication, sessions and tokens, single sign-on and OAuth in overview, and authorisation models and the principle of least privilege.

**Definition:** Authentication is the process of verifying that a user or system is who it claims to be, and authorisation is the process of determining what an authenticated identity is permitted to do, enforced consistently on every request.

<!--
IMAGE PROMPT  ->  generate as images/06_intro_authentication_and_authorization.png   (16:9 cinematic hero image, place here, right after the Introduction)

CHARACTER & THEME: Software Engineering course introduction image based on the central concept of this lesson. Show the core idea of the lesson visually, with no named characters.

STYLE: world-class high-end 3D render, cinematic and vibrant, glossy soft 3D forms, blue software forms, green positive accents, orange secondary accents, red warnings, soft studio-gradient backdrop, minimal large labels.

SCENE: Two sequential gates: the first a door with an ID badge scanner labelled Authentication, the second a corridor with several doors, some open and some locked, labelled Authorization.

ON-IMAGE TEXT: show a short bold title "Authentication and Authorization" plus only these few labels, large and legible: Who? Then What?. Keep text minimal, no sentences.

GOAL: make the opening idea instantly clear and engaging while matching the existing reading-material image standards.
-->

## Authentication

### Factors

A **factor** is a kind of evidence of identity.

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Factor</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Meaning</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Examples</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Weaknesses</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Knowledge (something you know)</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A secret</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Password, PIN, security answer</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Guessable, reused, phished, leaked</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Possession (something you have)</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A device or object</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Phone, hardware security key, smart card, one-time code generator</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Can be lost or stolen; some codes can be intercepted</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Inherence (something you are)</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Biological traits</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Fingerprint, face</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Cannot be changed if stolen; error rates; privacy concerns</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Context (somewhere you are, how you behave)</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Signals from the situation</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Location, device recognition, typing behaviour</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Supporting evidence only</td>
    </tr>
  </tbody>
</table>

**Multi-factor authentication (MFA)** requires two or more different kinds of factor, so that stealing one is not enough. It blocks the great majority of automated account takeovers and should be required for administrators and offered to all users. Not all second factors are equal: hardware keys and app-based approvals built on public-key cryptography (such as **passkeys** and the **FIDO2/WebAuthn** standards) resist phishing; text-message codes are better than nothing but can be intercepted or diverted.

### Passwords

Passwords remain the most common factor, and they are a source of constant trouble: people choose weak ones, reuse them across sites, and are fooled into revealing them.

**For users and policies:**

- Prefer **length** over complexity rules; encourage long passphrases.
- Check candidates against lists of known breached or common passwords.
- Permit password managers (do not block pasting).
- Do not force frequent changes without cause; require change after evidence of compromise.
- Limit and slow repeated attempts; lock or challenge after repeated failures without allowing attackers to lock out legitimate users easily.
- Offer MFA.

**For storage by the system:**

- **Never store passwords in readable form,** and never use reversible encryption for them.
- Store only the output of a **slow, salted, one-way hash** designed for password storage. A **hash** is a fixed-length fingerprint computed from the password that cannot be reversed. A **salt** is a unique random value added for each user so that identical passwords give different results and precomputed tables are useless. Use dedicated password-hashing functions (such as bcrypt, scrypt, or Argon2) that are deliberately costly to compute, which makes guessing slow even for an attacker who steals the database. General-purpose fast hashes are unsuitable.
- When a user logs in, the system hashes the entered password in the same way and compares.
- Protect the process for **recovery** as carefully as the login: a weak reset flow is a back door.

### Other Methods

- **Single sign-on (SSO):** a user authenticates once with a central identity provider and gains access to several applications. It reduces the number of passwords and centralises control.
- **Passwordless sign-in** with links, codes, or passkeys.
- **Certificates and keys** for machines and services (mutual authentication).
- **API keys:** simple secrets that identify an application; suitable for identification of a calling application, but weak as proof of a user's identity, and must be protected as secrets.
- **Biometrics** on devices, usually unlocking a local key rather than being sent over the network.

### Advice

Do not build authentication from scratch. Use a mature identity provider or a well-reviewed framework, which will handle storage, resets, MFA, and defences against common attacks.

## Sessions and Tokens

The web is built on requests that do not remember each other. After a user logs in, the system must recognise later requests as belonging to the same authenticated user. Two main mechanisms exist.

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Mechanism</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">How it works</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Strengths</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Cautions</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Server-side sessions</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">The server stores session data and gives the browser an unguessable identifier, usually in a cookie; the identifier is presented with each request</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Easy to revoke; data stays on the server</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Needs shared storage when many servers are used</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Tokens (for example signed JSON Web Tokens)</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">The server issues a signed token containing claims about the user; later requests present it, and any server can verify it</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Stateless; suits distributed services and APIs</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Hard to revoke before expiry; contents are readable unless encrypted; theft gives full use until expiry</td>
    </tr>
  </tbody>
</table>

Good practice for both:

- Use **long, random, unpredictable** identifiers generated by a secure source.
- Transmit only over encrypted connections.
- Mark cookies as inaccessible to scripts, sent only over secure connections, and restricted to same-site use, where applicable.
- Set **expiry** and idle time-outs; use short-lived access tokens with refresh arrangements.
- **Regenerate** the identifier at login and at privilege changes to prevent session fixation.
- Provide **logout** that invalidates server-side state.
- Protect against theft: guard against script injection, and monitor for unusual use.
- **Re-authenticate** before sensitive actions, such as changing a password or making a large payment.

## Delegated Access: OAuth and OpenID Connect (Overview)

Often one application needs to act on a user's behalf at another service, such as a calendar app reading a user's contacts, without being given the user's password. **OAuth 2.0** is the standard for this delegation.

- The user authenticates with the service that holds the data (the **authorisation server**) and **consents** to give the application limited access (**scopes**).
- The application receives an **access token,** limited in scope and lifetime, and uses it to call the service. It never sees the user's password.
- The user can revoke the access later.

**OpenID Connect** adds an identity layer on top of OAuth, letting an application learn who the user is from the identity provider; it powers "sign in with" buttons. Different **flows** suit different applications (for example, web servers, single-page apps, mobile apps, and machine-to-machine); current guidance favours the authorisation code flow with extra proof of possession, and discourages older flows. Implementers should use maintained libraries and follow current security recommendations rather than the original specifications alone.

## Authorisation

After identity is known, every action is checked against a policy.

### Models

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Model</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Idea</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Suits</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Access control lists (ACLs)</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Each resource carries a list of who may do what</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Files, documents with individual sharing</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Role-based access control (RBAC)</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Permissions attach to roles (customer, cook, manager, administrator); users are assigned roles</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Most business applications</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Attribute-based access control (ABAC)</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Decisions use attributes of the user, resource, action, and environment (department, data sensitivity, time, location)</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Fine-grained and context-dependent rules</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Relationship-based access control</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Access follows relationships in a graph (owner, member of a group, collaborator)</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Social, collaborative, and document-sharing systems</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Ownership checks</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">The user may act on their own objects only</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Every user-owned resource</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Policy engines</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Rules held in a separate, auditable policy service</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Large systems with consistent rules</td>
    </tr>
  </tbody>
</table>

### Principles

- **Least privilege:** grant the minimum; users, services, and database accounts alike.
- **Deny by default.**
- **Check on the server, on every request, for every object and action** (complete mediation). Hiding a button is not authorisation.
- **Check at the right level:** the function (may they call this?), the object (may they touch this record?), and the field (may they change this property?).
- **Centralise** the logic so that rules are written once and cannot be forgotten in a new endpoint.
- **Separation of duties:** sensitive operations need more than one person, such as one who requests and another who approves.
- **Time-limited elevation:** administrative rights granted for a task and then withdrawn.
- **Review permissions regularly** and remove those no longer needed.
- **Log** authorisation decisions, especially denials.
- **Test** that each role can do what it should and, as importantly, cannot do what it should not.

### Service-to-Service Trust

In distributed systems, services need identities and permissions too. Use service credentials with narrow scopes, mutual authentication, short-lived tokens, and network segmentation. The idea of **zero trust** applies: being inside the network is not proof of legitimacy.

## Common Mistakes

- Treating a hidden page as protected.
- Checking permission when a page loads but not when the action is submitted.
- Trusting identifiers or role claims sent by the client.
- Using the same powerful database account for the whole application.
- Writing a custom password scheme.
- Long-lived tokens without revocation.
- Neglecting account recovery and support procedures, which attackers use to take accounts.
- Giving users the same error for unknown user and wrong password is good; different messages let attackers discover valid accounts.

<!--
IMAGE PROMPT  ->  generate as images/06_authn_vs_authz_and_oauth.png   (16:9 explanatory diagram, place here)

Left: two gates in sequence for authentication with factors icons (password, phone, fingerprint) and authorisation with a role matrix. Right: a three-party OAuth flow with user, application, and service, arrows labelled Consent, Token, Access, and no password passed to the application.

STYLE: clean flat-3D infographic, blue primary forms, green for correct or healthy, orange for caution, red for failure, large legible labels, minimal text.
-->

## Your Turn: Prove It, Then Permit It

1. A site stores passwords with reversible encryption "so that support can help users who forget". What is wrong, and what should it do?
2. A user logged in as a normal customer types the address of the staff dashboard and sees it. Which control is missing?
3. A calendar app wants to read a user's contacts. Why is OAuth better than asking for the user's password?

For case 1, passwords must be stored only as salted, slow one-way hashes; forgotten passwords are handled by reset flows, never by revealing the original. For case 2, server-side authorisation on the dashboard (role check), because authentication alone does not decide permissions. For case 3, the application never sees the password, receives limited and revocable access, and the user can withdraw consent.

## Conclusion

Authentication is the process of verifying that a user or system is who it claims to be, and authorisation is the process of determining what an authenticated identity is permitted to do, enforced consistently on every request. Strong, standard mechanisms for each, with least privilege, deny by default, and server-side checks, prevent the account takeovers and unauthorised access that dominate real breaches.

These mechanisms depend on secrets and on cryptography, and on the many components that software relies on. The next topic covers secrets, cryptography, and dependencies.
