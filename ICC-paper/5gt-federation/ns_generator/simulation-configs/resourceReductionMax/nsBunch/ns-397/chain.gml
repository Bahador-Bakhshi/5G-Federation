graph [
  node [
    id 0
    label 1
    disk 3
    cpu 1
    memory 1
  ]
  node [
    id 1
    label 2
    disk 3
    cpu 2
    memory 5
  ]
  node [
    id 2
    label 3
    disk 6
    cpu 4
    memory 3
  ]
  node [
    id 3
    label 4
    disk 1
    cpu 1
    memory 2
  ]
  node [
    id 4
    label 5
    disk 6
    cpu 1
    memory 16
  ]
  node [
    id 5
    label 6
    disk 8
    cpu 3
    memory 11
  ]
  node [
    id 6
    label "start"
  ]
  edge [
    source 0
    target 6
    delay 25
    bw 97
  ]
  edge [
    source 0
    target 1
    delay 25
    bw 52
  ]
  edge [
    source 0
    target 2
    delay 35
    bw 74
  ]
  edge [
    source 1
    target 3
    delay 34
    bw 87
  ]
  edge [
    source 2
    target 3
    delay 26
    bw 191
  ]
  edge [
    source 3
    target 4
    delay 32
    bw 149
  ]
  edge [
    source 4
    target 5
    delay 26
    bw 165
  ]
]
