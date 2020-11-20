# Mermaid

[Mermaid](https://mermaid-js.github.io/) is a code-based UML diagram generator with markdown support on [popular platforms](https://mermaid-js.github.io/mermaid/#/./integrations) like GitLab, Azure DevOps and many others.

## Table of Contents

* [Graph](#graph)
  * [Node shapes](#node-shapes)
* [Flowchart](#flowchart)
  * [Link Between Nodes](#link-between-nodes)
  * [Orientation](#orientation)
  * [Subgraphs](#subgraphs)

## Graph

### Node shapes

```mermaid
graph TB
  %% This is a comment.
  %% Default shape is a square box that uses the node id as the text content.
  n1

  %% Square node with custom text
  n2[node N2]

  %% Other shapes
  n3(n3)
  n4[(n4)]
  n5([node n5])
  n6[[n6]]
  n7((n7))
  n8>n8]
  n9{n9}
  n10{{n10}}
  n11[/n11/]
  n12[\n12\]
  n13[/n13\]
  n14[\n14/]

  n1 --- n2 --- n3 ---
  n4 --- n5 --- n6 --- n7

  n8 --- n9 --- n10 ---
  n11 --- n12 --- n13 --- n14
```

## Flowchart

### Link between nodes

Link types:

```mermaid
graph LR
  a --- b
  a --> c
  a ---|Text| d
  a -.-|Text| e
  a ===|Text| f
  a ==>|Text| g

  %% Beta types
  a <--> h
  a --o i
  a --x j

```

Longer links:

| Length | 1 | 2 | 3 |
|-|-|-|-|
| Normal | --- | ---- | ----- |
| Normal with arrow | --> | ---> | ----> |
| Thick | === | ==== | ===== |
| Thick with arrow | ==> | ===> | ====> |
| Dotted | -.- | -..- | -...- |
| Dotted with arrow | -.-> | -..-> | -...-> |

```mermaid
graph TB
  a --> b -.-> c
  a ----> d
```

Multiple links:

```mermaid
graph LR
  a --> b & c & d -.-> e
  n1 & n2 --> n3 & n4
```

### Orientation

Top Bottom:

```mermaid
graph TB
  A[Node A text]
  A-->B
  A-->C
```

Bottom Top:

```mermaid
graph BT
  A[Node A text]
  A-->B
  A-->C
```

Left Right:

```mermaid
graph LR
  A[Node A text]
  A-->B
  A-->C
```

Right Left:

```mermaid
graph RL
  A[Node A text]
  A-->B
  A-->C
```

### Subgraphs

```mermaid
graph LR

  subgraph cluster
  a
  d
  end

  subgraph switch
  b ---|text| c
  end

  a ==> b
  c ==> d

  style cluster fill:#a3c,stroke:#fff,stroke-width:2px
  style switch fill:#666,stroke:#fff,stroke-width:2px

  %% Link styles are references by the order they were defined. Indexed from zero.
  linkStyle 0 stroke:#ff3,stroke-width:4px

```
