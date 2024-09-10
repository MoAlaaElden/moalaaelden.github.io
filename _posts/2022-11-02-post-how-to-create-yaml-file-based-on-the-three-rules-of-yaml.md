---
title: "How To Create YAML file based on The Three Rules of YAML"
header:
  image: /assets/images/yaml-file.webp
last_modified_at: 2022-11-02
categories:
  - Python
  - YAML
  - JSON
  - Network-Automation
tags:
  - Python
  - YAML
  - JSON
  - Network-Automation
toc: true # On this page
toc_sticky: true # Sticky Table of Contents
---
# How To Create YAML file based on The Three Rules of YAML

## What Is YAML?

- YAML stands for `yet another markup language` or `YAML ain’t markup language`.
- YAML is a `human-readable` and `human-friendly` data representation language.
- Mainly used for `configuration files` and internet messaging.
- It is useful to manage data and includes Unicode printable characters.
- YAML uses the `.yaml` extension for its files.

## YAML file consists of the following data types:

- **Scalars**: Scalars are values like **Strings, Integers, Booleans**, etc.
- **Sequences**: Sequences are lists with each item starting with a **hyphen(–)**. (Lists can also be nested).
- **Mappings**: Mapping gives the ability to list keys with values.

## The Three Rules of YAML

### Rule 1: Indentation

- YAML uses a **fixed indentation** scheme to represent relationshipsbetween data layers.
- **Whitespace indentation** is used to indicate nesting and overallstructure.

```yaml
---
ios:
  platform: ios
  connection_options:
    netmiko:
      platform: cisco_ios
      extras:
        global_delay_factor: 5
nxos:
  platform: nxos
  connection_options:
    netmiko:
      platform: cisco_nxos
      extras:
        global_delay_factor: 5
```
### Rule 2: Colons

- **Colons** are used in YAML to represent hashes, or associative arrays.
- In other words, **one-to-one mappings** between a **key** and a **value**.
- For example, to assign the **value xe-0/0/0** to the **interface_name** field:

```yaml
interface_name: xe-0/0/0
```
The same rule can be extended to a higher level and use **nested key-value** pairs where we can notice the usage of the indentation:

```yaml
interface:
  name: xe-0/0/0
  shutdown: false
  subinterfaces:
    xe-0/0/0.0:
      ipv4:
        address: 172.17.17.1/24
```
### Rule 3: Dashes

- Dashes are used to **represent a list of items**.
- Note the **single space** following the **hyphen**. For example:

```yaml
interfaces:
  - fa1/0/0
  - fa4/0/0
  - fa5/0/0
```

## YAML vs JSON

- Basically, both **JSON** and **YAML** are developed to provide a **human-readable** data interchange format. 
- The YAML is realized as a superset of JSON format.
- It means that we can parse JSON using a YAML parser.
- Although the practical implementation of this theory is little tricky.
- Therefore, some **basic differences between YAML and JSON** are given- below:

<figure class="wp-block-table"><table><thead><tr><th>YAML</th><th>JSON</th></tr></thead><tbody><tr><td>Complex and time-consuming process of parsing Serialized data</td><td>Quickly and easily parse JSON serialized data with its simpler design</td></tr><tr><td>Less community support</td><td>Larger community support and popularity</td></tr><tr><td>Supports comments</td><td>Doesn’t support comments</td></tr><tr><td>Ability to use reference of other data objects</td><td>Impossible to serialize complex structures with object references</td></tr><tr><td>Hierarchy is denoted by using double space characters. Tab characters are not allowed</td><td>Objects and Arrays are denoted in braces and brackets.</td></tr><tr><td>String quotes are optional but it supports single and double quotes.</td><td>Strings must be in double quotes.</td></tr><tr><td>Root node can be any of the valid data types</td><td>Root node must either be an array or an object.</td></tr></tbody></table><figcaption>Source: <a href="https://docs.fileformat.com/programming/yaml/" rel="nofollow">https://docs.fileformat.com/programming/yaml/</a></figcaption></figure>