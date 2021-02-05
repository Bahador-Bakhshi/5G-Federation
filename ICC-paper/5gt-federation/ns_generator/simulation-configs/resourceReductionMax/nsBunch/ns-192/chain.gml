graph [
  node [
    id 0
    label 1
    disk 3
    cpu 2
    memory 11
  ]
  node [
    id 1
    label 2
    disk 4
    cpu 4
    memory 12
  ]
  node [
    id 2
    label 3
    disk 6
    cpu 4
    memory 8
  ]
  node [
    id 3
    label 4
    disk 6
    cpu 2
    memory 9
  ]
  node [
    id 4
    label 5
    disk 4
    cpu 1
    memory 10
  ]
  node [
    id 5
    label 6
    disk 7
    cpu 2
    memory 15
  ]
  node [
    id 6
    label "start"
  ]
  edge [
    source 0
    target 6
    delay 31
    bw 120
  ]
  edge [
    source 0
    target 1
    delay 29
    bw 62
  ]
  edge [
    source 0
    target 2
    delay 29
    bw 57
  ]
  edge [
    source 0
    target 3
    delay 31
    bw 197
  ]
  edge [
    source 1
    target 5
    delay 26
    bw 103
  ]
  edge [
    source 3
    target 4
    delay 28
    bw 81
  ]
]
