graph [
  node [
    id 0
    label 1
    disk 1
    cpu 1
    memory 3
  ]
  node [
    id 1
    label 2
    disk 10
    cpu 4
    memory 14
  ]
  node [
    id 2
    label 3
    disk 3
    cpu 1
    memory 1
  ]
  node [
    id 3
    label 4
    disk 6
    cpu 1
    memory 13
  ]
  node [
    id 4
    label 5
    disk 10
    cpu 4
    memory 9
  ]
  node [
    id 5
    label 6
    disk 5
    cpu 3
    memory 9
  ]
  node [
    id 6
    label "start"
  ]
  edge [
    source 0
    target 6
    delay 34
    bw 94
  ]
  edge [
    source 0
    target 1
    delay 27
    bw 138
  ]
  edge [
    source 1
    target 2
    delay 29
    bw 176
  ]
  edge [
    source 1
    target 3
    delay 25
    bw 57
  ]
  edge [
    source 1
    target 4
    delay 30
    bw 59
  ]
  edge [
    source 4
    target 5
    delay 33
    bw 189
  ]
]
