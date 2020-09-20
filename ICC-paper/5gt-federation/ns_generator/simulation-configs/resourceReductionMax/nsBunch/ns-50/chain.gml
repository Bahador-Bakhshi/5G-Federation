graph [
  node [
    id 0
    label 1
    disk 3
    cpu 4
    memory 13
  ]
  node [
    id 1
    label 2
    disk 10
    cpu 3
    memory 9
  ]
  node [
    id 2
    label 3
    disk 10
    cpu 2
    memory 4
  ]
  node [
    id 3
    label 4
    disk 7
    cpu 3
    memory 6
  ]
  node [
    id 4
    label 5
    disk 6
    cpu 4
    memory 11
  ]
  node [
    id 5
    label 6
    disk 10
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
    delay 34
    bw 52
  ]
  edge [
    source 0
    target 1
    delay 28
    bw 73
  ]
  edge [
    source 0
    target 2
    delay 35
    bw 57
  ]
  edge [
    source 1
    target 3
    delay 29
    bw 99
  ]
  edge [
    source 2
    target 3
    delay 27
    bw 117
  ]
  edge [
    source 3
    target 4
    delay 32
    bw 191
  ]
  edge [
    source 4
    target 5
    delay 29
    bw 91
  ]
]
