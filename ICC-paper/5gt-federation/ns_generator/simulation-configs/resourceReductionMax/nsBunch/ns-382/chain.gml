graph [
  node [
    id 0
    label 1
    disk 10
    cpu 2
    memory 12
  ]
  node [
    id 1
    label 2
    disk 10
    cpu 2
    memory 1
  ]
  node [
    id 2
    label 3
    disk 3
    cpu 1
    memory 1
  ]
  node [
    id 3
    label 4
    disk 3
    cpu 3
    memory 8
  ]
  node [
    id 4
    label 5
    disk 6
    cpu 3
    memory 11
  ]
  node [
    id 5
    label 6
    disk 8
    cpu 2
    memory 8
  ]
  node [
    id 6
    label "start"
  ]
  edge [
    source 0
    target 6
    delay 30
    bw 126
  ]
  edge [
    source 0
    target 1
    delay 29
    bw 191
  ]
  edge [
    source 1
    target 2
    delay 30
    bw 149
  ]
  edge [
    source 2
    target 3
    delay 35
    bw 58
  ]
  edge [
    source 3
    target 4
    delay 28
    bw 90
  ]
  edge [
    source 3
    target 5
    delay 32
    bw 98
  ]
]
