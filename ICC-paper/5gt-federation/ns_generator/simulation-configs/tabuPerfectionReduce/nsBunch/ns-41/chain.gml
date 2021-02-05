graph [
  node [
    id 0
    label 1
    disk 2
    cpu 4
    memory 12
  ]
  node [
    id 1
    label 2
    disk 10
    cpu 2
    memory 4
  ]
  node [
    id 2
    label 3
    disk 10
    cpu 3
    memory 5
  ]
  node [
    id 3
    label 4
    disk 3
    cpu 1
    memory 11
  ]
  node [
    id 4
    label 5
    disk 8
    cpu 1
    memory 8
  ]
  node [
    id 5
    label 6
    disk 3
    cpu 2
    memory 12
  ]
  node [
    id 6
    label "start"
  ]
  edge [
    source 0
    target 6
    delay 27
    bw 76
  ]
  edge [
    source 0
    target 1
    delay 35
    bw 186
  ]
  edge [
    source 1
    target 2
    delay 25
    bw 103
  ]
  edge [
    source 1
    target 3
    delay 29
    bw 169
  ]
  edge [
    source 1
    target 4
    delay 26
    bw 126
  ]
  edge [
    source 3
    target 5
    delay 34
    bw 67
  ]
]
