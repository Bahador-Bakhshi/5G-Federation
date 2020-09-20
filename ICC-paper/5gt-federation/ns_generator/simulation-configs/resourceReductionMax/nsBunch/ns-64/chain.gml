graph [
  node [
    id 0
    label 1
    disk 9
    cpu 2
    memory 14
  ]
  node [
    id 1
    label 2
    disk 3
    cpu 2
    memory 8
  ]
  node [
    id 2
    label 3
    disk 3
    cpu 1
    memory 15
  ]
  node [
    id 3
    label 4
    disk 9
    cpu 1
    memory 10
  ]
  node [
    id 4
    label 5
    disk 6
    cpu 4
    memory 8
  ]
  node [
    id 5
    label 6
    disk 4
    cpu 2
    memory 5
  ]
  node [
    id 6
    label "start"
  ]
  edge [
    source 0
    target 6
    delay 28
    bw 110
  ]
  edge [
    source 0
    target 1
    delay 30
    bw 134
  ]
  edge [
    source 0
    target 2
    delay 27
    bw 118
  ]
  edge [
    source 0
    target 3
    delay 32
    bw 89
  ]
  edge [
    source 1
    target 4
    delay 26
    bw 178
  ]
  edge [
    source 2
    target 5
    delay 32
    bw 126
  ]
]
