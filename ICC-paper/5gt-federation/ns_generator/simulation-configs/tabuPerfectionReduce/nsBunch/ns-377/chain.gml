graph [
  node [
    id 0
    label 1
    disk 8
    cpu 4
    memory 11
  ]
  node [
    id 1
    label 2
    disk 8
    cpu 3
    memory 6
  ]
  node [
    id 2
    label 3
    disk 1
    cpu 1
    memory 11
  ]
  node [
    id 3
    label 4
    disk 7
    cpu 3
    memory 15
  ]
  node [
    id 4
    label 5
    disk 8
    cpu 2
    memory 10
  ]
  node [
    id 5
    label 6
    disk 2
    cpu 2
    memory 6
  ]
  node [
    id 6
    label "start"
  ]
  edge [
    source 0
    target 6
    delay 34
    bw 167
  ]
  edge [
    source 0
    target 1
    delay 34
    bw 92
  ]
  edge [
    source 0
    target 2
    delay 35
    bw 69
  ]
  edge [
    source 1
    target 4
    delay 27
    bw 69
  ]
  edge [
    source 2
    target 3
    delay 29
    bw 124
  ]
  edge [
    source 4
    target 5
    delay 27
    bw 172
  ]
]
