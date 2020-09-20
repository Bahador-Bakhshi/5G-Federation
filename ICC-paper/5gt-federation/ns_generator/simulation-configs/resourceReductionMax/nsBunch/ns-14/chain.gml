graph [
  node [
    id 0
    label 1
    disk 1
    cpu 4
    memory 6
  ]
  node [
    id 1
    label 2
    disk 3
    cpu 3
    memory 15
  ]
  node [
    id 2
    label 3
    disk 7
    cpu 1
    memory 5
  ]
  node [
    id 3
    label 4
    disk 5
    cpu 1
    memory 13
  ]
  node [
    id 4
    label 5
    disk 1
    cpu 3
    memory 6
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
    delay 28
    bw 91
  ]
  edge [
    source 0
    target 1
    delay 26
    bw 66
  ]
  edge [
    source 0
    target 2
    delay 33
    bw 81
  ]
  edge [
    source 1
    target 4
    delay 28
    bw 115
  ]
  edge [
    source 2
    target 3
    delay 27
    bw 52
  ]
  edge [
    source 4
    target 5
    delay 32
    bw 61
  ]
]
