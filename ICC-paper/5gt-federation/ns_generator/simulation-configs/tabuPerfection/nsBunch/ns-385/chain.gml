graph [
  node [
    id 0
    label 1
    disk 6
    cpu 4
    memory 14
  ]
  node [
    id 1
    label 2
    disk 10
    cpu 3
    memory 5
  ]
  node [
    id 2
    label 3
    disk 7
    cpu 3
    memory 11
  ]
  node [
    id 3
    label 4
    disk 6
    cpu 1
    memory 14
  ]
  node [
    id 4
    label 5
    disk 8
    cpu 1
    memory 13
  ]
  node [
    id 5
    label 6
    disk 3
    cpu 3
    memory 1
  ]
  node [
    id 6
    label "start"
  ]
  edge [
    source 0
    target 6
    delay 26
    bw 195
  ]
  edge [
    source 0
    target 1
    delay 26
    bw 68
  ]
  edge [
    source 1
    target 2
    delay 29
    bw 58
  ]
  edge [
    source 1
    target 3
    delay 35
    bw 182
  ]
  edge [
    source 1
    target 4
    delay 30
    bw 79
  ]
  edge [
    source 3
    target 5
    delay 35
    bw 90
  ]
]
