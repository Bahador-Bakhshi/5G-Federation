graph [
  node [
    id 0
    label 1
    disk 5
    cpu 1
    memory 15
  ]
  node [
    id 1
    label 2
    disk 4
    cpu 3
    memory 4
  ]
  node [
    id 2
    label 3
    disk 4
    cpu 3
    memory 7
  ]
  node [
    id 3
    label 4
    disk 8
    cpu 4
    memory 15
  ]
  node [
    id 4
    label 5
    disk 3
    cpu 4
    memory 8
  ]
  node [
    id 5
    label 6
    disk 9
    cpu 4
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
    bw 81
  ]
  edge [
    source 0
    target 1
    delay 35
    bw 100
  ]
  edge [
    source 1
    target 2
    delay 34
    bw 137
  ]
  edge [
    source 1
    target 3
    delay 30
    bw 167
  ]
  edge [
    source 1
    target 4
    delay 30
    bw 174
  ]
  edge [
    source 3
    target 5
    delay 32
    bw 136
  ]
]
