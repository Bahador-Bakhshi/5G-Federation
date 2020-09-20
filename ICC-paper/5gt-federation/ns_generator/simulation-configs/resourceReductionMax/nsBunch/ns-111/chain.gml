graph [
  node [
    id 0
    label 1
    disk 1
    cpu 1
    memory 1
  ]
  node [
    id 1
    label 2
    disk 7
    cpu 1
    memory 9
  ]
  node [
    id 2
    label 3
    disk 6
    cpu 2
    memory 14
  ]
  node [
    id 3
    label 4
    disk 2
    cpu 4
    memory 14
  ]
  node [
    id 4
    label 5
    disk 4
    cpu 1
    memory 2
  ]
  node [
    id 5
    label 6
    disk 5
    cpu 1
    memory 11
  ]
  node [
    id 6
    label "start"
  ]
  edge [
    source 0
    target 6
    delay 28
    bw 64
  ]
  edge [
    source 0
    target 1
    delay 34
    bw 96
  ]
  edge [
    source 0
    target 2
    delay 34
    bw 191
  ]
  edge [
    source 0
    target 3
    delay 29
    bw 53
  ]
  edge [
    source 2
    target 4
    delay 30
    bw 198
  ]
  edge [
    source 3
    target 5
    delay 30
    bw 194
  ]
]
