graph [
  node [
    id 0
    label 1
    disk 1
    cpu 2
    memory 3
  ]
  node [
    id 1
    label 2
    disk 5
    cpu 3
    memory 11
  ]
  node [
    id 2
    label 3
    disk 6
    cpu 3
    memory 8
  ]
  node [
    id 3
    label 4
    disk 2
    cpu 4
    memory 5
  ]
  node [
    id 4
    label 5
    disk 10
    cpu 3
    memory 9
  ]
  node [
    id 5
    label 6
    disk 7
    cpu 2
    memory 11
  ]
  node [
    id 6
    label "start"
  ]
  edge [
    source 0
    target 6
    delay 32
    bw 168
  ]
  edge [
    source 0
    target 1
    delay 29
    bw 175
  ]
  edge [
    source 1
    target 2
    delay 29
    bw 137
  ]
  edge [
    source 1
    target 3
    delay 34
    bw 62
  ]
  edge [
    source 1
    target 4
    delay 30
    bw 171
  ]
  edge [
    source 2
    target 5
    delay 33
    bw 164
  ]
  edge [
    source 3
    target 5
    delay 33
    bw 142
  ]
  edge [
    source 4
    target 5
    delay 33
    bw 176
  ]
]
