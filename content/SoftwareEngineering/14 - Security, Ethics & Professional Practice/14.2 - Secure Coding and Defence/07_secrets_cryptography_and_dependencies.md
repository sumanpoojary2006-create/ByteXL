## Introduction

Software depends on things that must stay secret, such as passwords, keys, and tokens; on mathematics that protects information, cryptography; and on other people's code, libraries and services. Each is a rich source of failures. Credentials committed to a public repository are collected by automated scanners within minutes; home-made cryptography is almost always broken; and a single compromised library can reach thousands of products. Handling these three subjects well does not require expertise in the mathematics; it requires knowing a small number of rules and sticking to them.

This topic explains how to manage secrets, what cryptography does and which tools to use for which job, the difference between hashing and encryption, and how to manage the supply chain of third-party components.

**Definition:** Secrets management is the controlled creation, storage, distribution, rotation, and revocation of credentials and keys; cryptography is the use of mathematical techniques to protect the confidentiality, integrity, and authenticity of information; and supply-chain security is the practice of ensuring that the third-party code, tools, and services a product depends on are trustworthy and kept up to date.

<!--
IMAGE PROMPT  ->  generate as images/07_intro_secrets_cryptography_and_dependencies.png   (16:9 cinematic hero image, place here, right after the Introduction)

CHARACTER & THEME: Software Engineering course introduction image based on the central concept of this lesson. Show the core idea of the lesson visually, with no named characters.

STYLE: world-class high-end 3D render, cinematic and vibrant, glossy soft 3D forms, blue software forms, green positive accents, orange secondary accents, red warnings, soft studio-gradient backdrop, minimal large labels.

SCENE: Three panels: a key in a vault labelled Secrets, a lock with a mathematical glyph labelled Cryptography, and a chain of linked package boxes with one cracked link labelled Dependencies.

ON-IMAGE TEXT: show a short bold title "Secrets, Cryptography and Dependencies" plus only these few labels, large and legible: Keep, Protect, Trust. Keep text minimal, no sentences.

GOAL: make the opening idea instantly clear and engaging while matching the existing reading-material image standards.
-->

## Secrets

A **secret** is any value whose disclosure would allow unauthorised access: passwords, API keys, tokens, private keys, database connection strings, signing keys, and certificates.

### The Cardinal Rule

**Never put secrets in source code, configuration files in the repository, build logs, container images, or chat messages.** Version control keeps history forever (Unit 9), so a secret committed once must be considered exposed even after deletion. Public repositories are scanned continuously by attackers, and exposed cloud keys have been abused within minutes. Private repositories are also at risk through copies, former employees, and compromised accounts.

### Managing Secrets Properly

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Practice</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Purpose</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Use a secrets manager or vault</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Central, encrypted storage with access control and audit logs</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Inject secrets at runtime</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Supply secrets to the running application from the environment or manager, not baked into builds</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Give each service its own credentials with minimal scope</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Limits damage if one is stolen</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Prefer short-lived, automatically issued credentials</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Less to steal, less to rotate</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Rotate regularly and on suspicion</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Limits the window of exposure; rotation should be automated and rehearsed</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Revoke immediately when people leave or secrets leak</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Stops misuse</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Separate by environment</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Production secrets are not used in development or test</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Scan for secrets</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Automated scanning of code, history, and logs in the pipeline and on developer machines</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Keep secrets out of logs and error messages</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Avoids silent leaks</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Restrict human access</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Few people should be able to read production secrets</td>
    </tr>
  </tbody>
</table>

If a secret is leaked, the response is to **revoke and replace** it, then investigate use, never merely to delete the file.

## Cryptography

Cryptography provides four kinds of protection, which should not be confused.

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Goal</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Technique</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Meaning</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Confidentiality</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Encryption</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Only authorised parties can read the data</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Integrity</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Hashing, message authentication codes</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Any change to data can be detected</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Authenticity and non-repudiation</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Digital signatures</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">The data came from a particular party and was not altered</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Key agreement and identity</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Public-key exchange and certificates</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Parties can set up secure communication and trust identities</td>
    </tr>
  </tbody>
</table>

### Hashing versus Encryption

These are often confused.

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Aspect</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Hashing</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Encryption</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Direction</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">One-way: cannot be reversed</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Two-way: can be decrypted with the key</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Output</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Fixed-length fingerprint of the input</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Ciphertext, about the size of the input</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Key</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">None (or a secret key in a keyed hash)</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Required</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Purpose</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Verify integrity; store password verifiers; compare values without revealing them</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Protect data that must be read again later</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Example uses</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Password storage (with specialised functions), file checksums, digital signatures over a digest</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Protecting stored personal data, protecting communication</td>
    </tr>
  </tbody>
</table>

A good hash function gives very different outputs for tiny changes in input, and it is infeasible to find two inputs with the same output. Older algorithms that are now broken (such as MD5 and SHA-1) must not be used for security.

### Symmetric and Asymmetric Encryption

- **Symmetric encryption** uses one shared secret key to encrypt and decrypt. It is fast and used for bulk data. The current standard algorithm is **AES.** The difficulty lies in sharing the key safely.
- **Asymmetric (public-key) encryption** uses a pair of keys: a **public key,** which anyone may have, and a **private key,** which is kept secret. Data encrypted with the public key can only be decrypted with the private key. It solves the key-sharing problem but is slower, so it is used to exchange symmetric keys and for signatures. Common systems are RSA and elliptic-curve cryptography. The idea was published by Whitfield Diffie and Martin Hellman in 1976, followed by the RSA algorithm of Rivest, Shamir, and Adleman in 1977.
- **Digital signatures** use the private key to sign and the public key to verify, proving origin and integrity.
- **Certificates,** issued by trusted **certificate authorities,** bind a public key to an identity, such as a web domain. They underpin trust on the web.

### Encryption in Transit and at Rest

- **In transit:** Transport Layer Security (**TLS**), the protocol behind the padlock in a browser and HTTPS, protects data between client and server. Use current versions, valid certificates, and encryption on internal connections as well as external ones.
- **At rest:** disk, database, and backup encryption protect stored data if media or backups are stolen. Application-level encryption of especially sensitive fields adds protection even against some database administrators.
- **End-to-end encryption** protects messages so that only the communicating parties can read them, not even the service in the middle.

### Rules for Using Cryptography

1. **Do not invent your own algorithms or protocols.** Experts design them over years and still find flaws; amateurs fail quickly.
2. **Use high-level, well-reviewed libraries** with safe defaults, not low-level primitives. Many errors lie in how primitives are combined (modes, padding, nonces).
3. **Choose current, standard algorithms** and key sizes; plan to change them (**crypto-agility**), since algorithms age. Quantum computers may eventually break current public-key schemes, and standards bodies have begun to select replacements.
4. **Generate randomness with a cryptographically secure source;** ordinary random-number functions are predictable.
5. **Protect keys more carefully than data:** store in key management services or hardware security modules; separate from the data they protect; rotate; limit access.
6. **Verify certificates** and never switch off checks "to make it work".
7. **Do not roll your own password storage or token formats.**
8. **Encrypt only what needs it, and still minimise the data.** The strongest protection for data is not to hold it.

## Dependencies and the Supply Chain

### The Scale of Dependence

Most of an application's code is third-party. A typical modern application can contain hundreds or thousands of libraries, including indirect ones (**transitive dependencies**) that no developer chose consciously. Any of these may contain flaws or, worse, malicious code.

### Kinds of Risk

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Risk</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Description</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Example</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Known vulnerabilities</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A published flaw in a version you use</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A widely used logging library flaw in late 2021 forced emergency patching across industries</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Abandoned or unmaintained projects</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">No one fixes problems</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A small library whose maintainer has left</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Malicious packages</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Code created to harm</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Packages with names close to popular ones (typosquatting); a maintainer account taken over</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Dependency confusion</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A build is tricked into fetching a public package in place of a private one with the same name</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Internal package name registered publicly</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Compromised build or distribution</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Trusted updates replaced with harmful ones</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">The 2020 compromise of a network-management product's update process</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Protestware and sabotage</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A maintainer deliberately damages their own package</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Cases in which packages were altered to delete files or fail</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Licensing issues</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Terms incompatible with use</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Covered in the intellectual property topic</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Over-reliance on tiny packages</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Trivial functions pulled in from outside; one removed package can break many builds</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A 2016 incident in which the removal of a very small package disrupted large parts of the JavaScript ecosystem</td>
    </tr>
  </tbody>
</table>

### Controls

- **Know what you use:** maintain a **software bill of materials (SBOM)** listing every component and version.
- **Scan continuously** for known vulnerabilities (software composition analysis) and subscribe to advisories; services in the version control platform can open update proposals automatically.
- **Update regularly, in small steps,** supported by good automated tests (Unit 10); a team that updates monthly copes with updates far better than one that has not updated in three years.
- **Pin versions and use lock files** so that builds are reproducible and do not silently pick up new, unreviewed code; combine with regular, deliberate updates.
- **Verify integrity:** use checksums and signatures; fetch from trusted registries; configure private package names so that they cannot be shadowed.
- **Choose carefully:** prefer well-maintained, widely used projects with active security practices; consider the number of maintainers and the health of the project.
- **Reduce the footprint:** remove unused dependencies; avoid pulling in a large package for a trivial need.
- **Isolate and limit privileges** of build systems and runtime components; do not run builds with production secrets.
- **Protect the pipeline:** require review for changes to build scripts and dependencies, use short-lived credentials, and secure the build servers.
- **Have a plan for emergencies:** the ability to find all uses of a component in hours and to ship a patched version quickly.
- **Frameworks for assurance:** the SLSA framework (Supply-chain Levels for Software Artifacts) offers graded levels of build integrity.

<!--
IMAGE PROMPT  ->  generate as images/07_secrets_hashing_encryption_and_supply_chain.png   (16:9 explanatory diagram, place here)

Left: a repository box with a red key falling out of it versus a vault feeding a running service with a green key. Centre: a two-column comparison, Hash (one-way arrow) and Encrypt (two-way arrow with key). Right: a tree of dependencies with one red node and an SBOM list beside it.

STYLE: clean flat-3D infographic, blue primary forms, green for correct or healthy, orange for caution, red for failure, large legible labels, minimal text.
-->

## Your Turn: Protect and Trust

1. A developer commits a cloud access key to a repository and deletes it in the next commit. Is the problem solved?
2. A team needs to check a user's password at login and also to store a customer's date of birth so it can be shown later. Which technique suits each?
3. Why is it risky to leave dependencies unchanged for years?

For case 1, no: the key remains in history and may already have been harvested; revoke and replace it, and investigate use. For case 2, a slow, salted one-way hash for the password; encryption for the date of birth, which must be recovered. For case 3, known vulnerabilities accumulate, and a large backlog of updates is hard to apply quickly in an emergency; small regular updates are safer.

## Conclusion

Secrets management is the controlled creation, storage, distribution, rotation, and revocation of credentials and keys; cryptography is the use of mathematical techniques to protect the confidentiality, integrity, and authenticity of information; and supply-chain security is the practice of ensuring that the third-party code, tools, and services a product depends on are trustworthy and kept up to date. Following a few firm rules in each area prevents a great many breaches.

Controls and habits must be checked to show that they work. The next topic covers security testing and code review.
