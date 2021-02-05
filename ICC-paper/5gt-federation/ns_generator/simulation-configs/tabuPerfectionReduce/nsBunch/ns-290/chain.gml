graph [
  node [
    id 0
    label 1
    disk 5
    cpu 2
    memory 11
  ]
  node [
    id 1
    label 2
    disk 7
    cpu 3
    memory 8
  ]
  node [
    id 2
    label 3
    disk 5
    cpu 3
    memory 11
  ]
  node [
    id 3
    label 4
    disk 5
    cpu 3
    memory 5
  ]
  node [
    id 4
    label 5
    disk 3
    cpu 4
    memory 1
  ]
  node [
    id 5
    label 6
    disk 7
    cpu 2
    memory 2
  ]
  node [
    id 6
    label "start"
  ]
  edge [
    source 0
    target 6
    delay 28
    bw 104
  ]
  edge [
    source 0
    target 1
    delay 26
    bw 115
  ]
  edge [
    source 1
    target 2
    delay 28
    bw 176
  ]
  edge [
    source 2
    target 3
    delay 29
    bw 135
  ]
  edge [
    source 3
    target 4
    delay 30
    bw 101
  ]
  edge [
    source 3
    target 5
    delay 26
    bw 85
  ]
]
