graph [
  node [
    id 0
    label 1
    disk 5
    cpu 4
    memory 14
  ]
  node [
    id 1
    label 2
    disk 2
    cpu 3
    memory 7
  ]
  node [
    id 2
    label 3
    disk 4
    cpu 3
    memory 5
  ]
  node [
    id 3
    label 4
    disk 1
    cpu 1
    memory 16
  ]
  node [
    id 4
    label 5
    disk 6
    cpu 1
    memory 15
  ]
  node [
    id 5
    label 6
    disk 7
    cpu 1
    memory 1
  ]
  node [
    id 6
    label "start"
  ]
  edge [
    source 0
    target 6
    delay 25
    bw 114
  ]
  edge [
    source 0
    target 1
    delay 28
    bw 120
  ]
  edge [
    source 0
    target 2
    delay 30
    bw 67
  ]
  edge [
    source 0
    target 3
    delay 30
    bw 53
  ]
  edge [
    source 1
    target 4
    delay 33
    bw 164
  ]
  edge [
    source 2
    target 4
    delay 31
    bw 138
  ]
  edge [
    source 3
    target 4
    delay 33
    bw 144
  ]
  edge [
    source 4
    target 5
    delay 25
    bw 56
  ]
]
