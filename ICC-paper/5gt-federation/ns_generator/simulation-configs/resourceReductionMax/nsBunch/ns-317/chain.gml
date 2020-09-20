graph [
  node [
    id 0
    label 1
    disk 4
    cpu 2
    memory 5
  ]
  node [
    id 1
    label 2
    disk 5
    cpu 4
    memory 15
  ]
  node [
    id 2
    label 3
    disk 9
    cpu 4
    memory 1
  ]
  node [
    id 3
    label 4
    disk 9
    cpu 2
    memory 10
  ]
  node [
    id 4
    label 5
    disk 8
    cpu 3
    memory 3
  ]
  node [
    id 5
    label 6
    disk 2
    cpu 4
    memory 11
  ]
  node [
    id 6
    label "start"
  ]
  edge [
    source 0
    target 6
    delay 30
    bw 167
  ]
  edge [
    source 0
    target 1
    delay 35
    bw 77
  ]
  edge [
    source 1
    target 2
    delay 35
    bw 71
  ]
  edge [
    source 2
    target 3
    delay 27
    bw 189
  ]
  edge [
    source 2
    target 4
    delay 28
    bw 126
  ]
  edge [
    source 3
    target 5
    delay 33
    bw 115
  ]
]
