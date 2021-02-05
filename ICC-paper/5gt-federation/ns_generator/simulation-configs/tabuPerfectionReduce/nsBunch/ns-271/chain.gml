graph [
  node [
    id 0
    label 1
    disk 1
    cpu 1
    memory 5
  ]
  node [
    id 1
    label 2
    disk 5
    cpu 4
    memory 9
  ]
  node [
    id 2
    label 3
    disk 4
    cpu 2
    memory 7
  ]
  node [
    id 3
    label 4
    disk 3
    cpu 4
    memory 16
  ]
  node [
    id 4
    label 5
    disk 4
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
    delay 25
    bw 145
  ]
  edge [
    source 0
    target 1
    delay 35
    bw 61
  ]
  edge [
    source 0
    target 2
    delay 26
    bw 76
  ]
  edge [
    source 0
    target 3
    delay 31
    bw 137
  ]
  edge [
    source 2
    target 4
    delay 31
    bw 84
  ]
  edge [
    source 4
    target 5
    delay 25
    bw 77
  ]
]
