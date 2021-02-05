graph [
  node [
    id 0
    label 1
    disk 8
    cpu 2
    memory 7
  ]
  node [
    id 1
    label 2
    disk 10
    cpu 3
    memory 13
  ]
  node [
    id 2
    label 3
    disk 8
    cpu 3
    memory 12
  ]
  node [
    id 3
    label 4
    disk 3
    cpu 1
    memory 13
  ]
  node [
    id 4
    label 5
    disk 8
    cpu 4
    memory 3
  ]
  node [
    id 5
    label 6
    disk 8
    cpu 2
    memory 13
  ]
  node [
    id 6
    label "start"
  ]
  edge [
    source 0
    target 6
    delay 35
    bw 154
  ]
  edge [
    source 0
    target 1
    delay 33
    bw 115
  ]
  edge [
    source 1
    target 2
    delay 32
    bw 56
  ]
  edge [
    source 2
    target 3
    delay 32
    bw 193
  ]
  edge [
    source 3
    target 4
    delay 32
    bw 101
  ]
  edge [
    source 3
    target 5
    delay 27
    bw 105
  ]
]
