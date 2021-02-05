graph [
  node [
    id 0
    label 1
    disk 5
    cpu 4
    memory 11
  ]
  node [
    id 1
    label 2
    disk 9
    cpu 3
    memory 4
  ]
  node [
    id 2
    label 3
    disk 1
    cpu 3
    memory 2
  ]
  node [
    id 3
    label 4
    disk 8
    cpu 1
    memory 4
  ]
  node [
    id 4
    label 5
    disk 2
    cpu 3
    memory 6
  ]
  node [
    id 5
    label 6
    disk 7
    cpu 1
    memory 7
  ]
  node [
    id 6
    label "start"
  ]
  edge [
    source 0
    target 6
    delay 28
    bw 140
  ]
  edge [
    source 0
    target 1
    delay 34
    bw 99
  ]
  edge [
    source 1
    target 2
    delay 35
    bw 78
  ]
  edge [
    source 1
    target 3
    delay 35
    bw 186
  ]
  edge [
    source 2
    target 4
    delay 26
    bw 81
  ]
  edge [
    source 3
    target 5
    delay 26
    bw 112
  ]
]
