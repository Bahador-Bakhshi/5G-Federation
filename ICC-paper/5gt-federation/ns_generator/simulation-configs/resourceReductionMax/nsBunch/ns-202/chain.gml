graph [
  node [
    id 0
    label 1
    disk 10
    cpu 4
    memory 12
  ]
  node [
    id 1
    label 2
    disk 10
    cpu 4
    memory 12
  ]
  node [
    id 2
    label 3
    disk 2
    cpu 3
    memory 4
  ]
  node [
    id 3
    label 4
    disk 1
    cpu 3
    memory 13
  ]
  node [
    id 4
    label 5
    disk 10
    cpu 4
    memory 11
  ]
  node [
    id 5
    label 6
    disk 8
    cpu 4
    memory 8
  ]
  node [
    id 6
    label "start"
  ]
  edge [
    source 0
    target 6
    delay 25
    bw 69
  ]
  edge [
    source 0
    target 1
    delay 25
    bw 55
  ]
  edge [
    source 0
    target 2
    delay 30
    bw 82
  ]
  edge [
    source 0
    target 3
    delay 28
    bw 65
  ]
  edge [
    source 1
    target 4
    delay 29
    bw 154
  ]
  edge [
    source 2
    target 4
    delay 29
    bw 67
  ]
  edge [
    source 3
    target 5
    delay 29
    bw 53
  ]
]
