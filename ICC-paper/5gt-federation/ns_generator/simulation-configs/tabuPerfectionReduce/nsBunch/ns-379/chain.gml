graph [
  node [
    id 0
    label 1
    disk 10
    cpu 1
    memory 5
  ]
  node [
    id 1
    label 2
    disk 6
    cpu 2
    memory 16
  ]
  node [
    id 2
    label 3
    disk 1
    cpu 3
    memory 14
  ]
  node [
    id 3
    label 4
    disk 5
    cpu 3
    memory 8
  ]
  node [
    id 4
    label 5
    disk 10
    cpu 1
    memory 12
  ]
  node [
    id 5
    label 6
    disk 5
    cpu 1
    memory 6
  ]
  node [
    id 6
    label "start"
  ]
  edge [
    source 0
    target 6
    delay 33
    bw 166
  ]
  edge [
    source 0
    target 1
    delay 31
    bw 78
  ]
  edge [
    source 1
    target 2
    delay 25
    bw 73
  ]
  edge [
    source 2
    target 3
    delay 33
    bw 110
  ]
  edge [
    source 2
    target 4
    delay 26
    bw 118
  ]
  edge [
    source 2
    target 5
    delay 26
    bw 118
  ]
]
