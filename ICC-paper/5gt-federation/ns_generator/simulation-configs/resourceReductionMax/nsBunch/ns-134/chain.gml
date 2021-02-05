graph [
  node [
    id 0
    label 1
    disk 2
    cpu 4
    memory 4
  ]
  node [
    id 1
    label 2
    disk 9
    cpu 3
    memory 15
  ]
  node [
    id 2
    label 3
    disk 9
    cpu 1
    memory 14
  ]
  node [
    id 3
    label 4
    disk 10
    cpu 3
    memory 11
  ]
  node [
    id 4
    label 5
    disk 1
    cpu 2
    memory 7
  ]
  node [
    id 5
    label 6
    disk 6
    cpu 1
    memory 6
  ]
  node [
    id 6
    label "start"
  ]
  edge [
    source 0
    target 6
    delay 32
    bw 75
  ]
  edge [
    source 0
    target 1
    delay 32
    bw 126
  ]
  edge [
    source 1
    target 2
    delay 27
    bw 191
  ]
  edge [
    source 2
    target 3
    delay 31
    bw 156
  ]
  edge [
    source 2
    target 4
    delay 26
    bw 63
  ]
  edge [
    source 2
    target 5
    delay 26
    bw 93
  ]
]
