graph [
  node [
    id 0
    label 1
    disk 3
    cpu 3
    memory 11
  ]
  node [
    id 1
    label 2
    disk 9
    cpu 4
    memory 9
  ]
  node [
    id 2
    label 3
    disk 5
    cpu 2
    memory 15
  ]
  node [
    id 3
    label 4
    disk 5
    cpu 1
    memory 11
  ]
  node [
    id 4
    label 5
    disk 6
    cpu 1
    memory 5
  ]
  node [
    id 5
    label 6
    disk 8
    cpu 3
    memory 4
  ]
  node [
    id 6
    label "start"
  ]
  edge [
    source 0
    target 6
    delay 29
    bw 68
  ]
  edge [
    source 0
    target 1
    delay 26
    bw 78
  ]
  edge [
    source 0
    target 2
    delay 27
    bw 77
  ]
  edge [
    source 1
    target 4
    delay 26
    bw 185
  ]
  edge [
    source 2
    target 3
    delay 35
    bw 97
  ]
  edge [
    source 4
    target 5
    delay 28
    bw 61
  ]
]
