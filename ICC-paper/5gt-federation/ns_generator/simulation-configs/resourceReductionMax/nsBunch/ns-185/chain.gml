graph [
  node [
    id 0
    label 1
    disk 9
    cpu 4
    memory 12
  ]
  node [
    id 1
    label 2
    disk 1
    cpu 3
    memory 16
  ]
  node [
    id 2
    label 3
    disk 10
    cpu 2
    memory 5
  ]
  node [
    id 3
    label 4
    disk 10
    cpu 1
    memory 15
  ]
  node [
    id 4
    label 5
    disk 8
    cpu 2
    memory 2
  ]
  node [
    id 5
    label 6
    disk 1
    cpu 1
    memory 13
  ]
  node [
    id 6
    label "start"
  ]
  edge [
    source 0
    target 6
    delay 30
    bw 104
  ]
  edge [
    source 0
    target 1
    delay 27
    bw 101
  ]
  edge [
    source 0
    target 2
    delay 30
    bw 66
  ]
  edge [
    source 1
    target 3
    delay 29
    bw 50
  ]
  edge [
    source 2
    target 3
    delay 28
    bw 171
  ]
  edge [
    source 3
    target 4
    delay 29
    bw 62
  ]
  edge [
    source 4
    target 5
    delay 34
    bw 181
  ]
]
